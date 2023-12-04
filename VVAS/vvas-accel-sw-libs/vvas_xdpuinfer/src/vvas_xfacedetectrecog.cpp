/*
 * Copyright 2020 Xilinx, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "vvas_xfacedetect.hpp"
#include "vvas_xfacerecog.hpp"
#include "vvas_xfacedetectrecog.hpp"
#include "common_functions.hpp"

vvas_xfacedetectrecog::vvas_xfacedetectrecog(vvas_xkpriv * kpriv, const std::string & model_name, bool need_preprocess) {
  log_level = kpriv->log_level;
  LOG_MESSAGE(LOG_LEVEL_INFO, log_level, "enter : create model");
  model_fd = vitis::ai::FaceDetect::create(model_name, need_preprocess);
  model_fr = vitis::ai::FaceFeature::create("InceptionResnetV1", false);
  LOG_MESSAGE(LOG_LEVEL_INFO, log_level, "enter : %s", kpriv->embeddings_npzpath.c_str());
  std::tie(embedding_arr, embedding_norm_arr, embedding_class_arr) = load_embeddings(kpriv->embeddings_npzpath);
  label_arr = get_label_array(kpriv);
}

int vvas_xfacedetectrecog::run(vvas_xkpriv * kpriv, std::vector<cv::Mat>& images, GstInferencePrediction **predictions) {
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "run : %d x %d", images[0].rows, images[0].cols);

  auto results_fd = model_fd->run(images);
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "size of results_fd : %d", results_fd.size());
  char *pstr; // prediction string

  if (kpriv->objs_detection_max > 0) {
    // LOG_MESSAGE (LOG_LEVEL_DEBUG, kpriv->log_level, "sort detected faces based on bbox area");
    /* sort objects based on dimension to pick objects with bigger bbox */
    for (unsigned int i = 0u; i < results_fd.size(); i++) {
      std::sort(results_fd[i].rects.begin(), results_fd[i].rects.end(), compare_bbox_by_area);
    }
  } else {
    LOG_MESSAGE(LOG_LEVEL_WARNING, kpriv->log_level, "max-objects count is zero. So, not doing any metadata processing");
    return true;
  }

  for (auto i = 0u; i < results_fd.size(); i++) {
    GstInferencePrediction *parent_predict = NULL; // _GstInferencePrediction{... guint64 prediction_id; BoundingBox bbox; GList * classifications; GNode * predictions; GstBuffer *sub_buffer; gboolean bbox_scaled; ...}
    unsigned int cur_faces = 0;

    if (results_fd[i].rects.size()) {
      BoundingBox parent_bbox;
      int cols = images[i].cols;
      int rows = images[i].rows;

      // predictions[i] : for return
      // parent_predict : old one so need to append(update) with new things
      // parent : new things
      parent_predict = predictions[i];
      LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "   results_fd[%d].rects size : %ld", i, results_fd[i].rects.size());
      for (auto &r : results_fd[i].rects) {

        if (!parent_predict) {
          parent_bbox.x = parent_bbox.y = 0;
          parent_bbox.width = cols;
          parent_bbox.height = rows;
          parent_predict = gst_inference_prediction_new_full(&parent_bbox);
        }

        if (r.score < 0.9) {
          LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "      detected face(%f) ignored by threshold(0.9)");
          continue;
        }

        float xmin = r.x * cols + 1;
        float ymin = r.y * rows + 1;
        float xmax = xmin + r.width * cols;
        float ymax = ymin + r.height * rows;
        if (xmin < 0.)
          xmin = 1.;
        if (ymin < 0.)
          ymin = 1.;
        if (xmax > cols)
          xmax = cols;
        if (ymax > rows)
          ymax = rows;

        BoundingBox bbox;
        GstInferencePrediction * predict;
        GstInferenceClassification *c = NULL;

        bbox.x = xmin;
        bbox.y = ymin;
        bbox.width = xmax - xmin;
        bbox.height = ymax - ymin;
        cv::Mat cropped_image = images[i](Range(ymin, ymax), Range(xmin, xmax));
        // cv::Mat resized_image;
        // cv::resize(cropped_image, resized_image, cv::Size(160, 160), INTER_LINEAR);
        LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "      DETECTED: %f %f %f %f (%f)", xmin, ymin, xmax, ymax, r.score);

        auto result = model_fr->run(cropped_image);
        float max_val = -1.0;
        int max_idx = 0;
        // std::tie(max_val, max_idx) = get_max_values(*result.feature, kpriv->num_labels);
        // LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "         RECOG feature max idx and value : %d / (%f)", max_idx, max_val);

        float embedding_max_val = -100.0;
        int embedding_max_idx = 0;
        float feature1_norm = feature_norm((*result.feature).data());
        for (int e=0; e<embedding_arr.size(); e++) {
          float feature2_norm = embedding_norm_arr[e];
          float dot = feature_dot((*result.feature).data(), embedding_arr[e].data());
          float cosine_sim = dot * feature1_norm * feature2_norm;
          if (cosine_sim > embedding_max_val) {
            embedding_max_val = cosine_sim;
            embedding_max_idx = e;
          }
        }
        std::string max_class = embedding_class_arr[embedding_max_idx];
        max_idx = std::find(label_arr.begin(), label_arr.end(), max_class) - label_arr.begin();
        max_val = embedding_max_val;
        LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "         RECOG feature max idx and value : %d / %s (%f)", max_idx, max_class.c_str(), max_val);

        // start to fill new one
        predict = gst_inference_prediction_new_full(&bbox);
        string label_display_name = kpriv->labelptr[max_idx].display_name;
        const char* label_display_name_char = label_display_name.c_str();
        c = gst_inference_classification_new_full(max_idx, max_val, label_display_name_char, kpriv->num_labels, NULL, NULL, NULL);
        gst_inference_prediction_append_classification(predict, c);

        if(parent_predict->predictions == NULL)
          LOG_MESSAGE(LOG_LEVEL_ERROR, kpriv->log_level, "         parent_predict->predictions is NULL");

        gst_inference_prediction_append(parent_predict, predict);

        pstr = gst_inference_prediction_to_string(parent_predict);
        LOG_MESSAGE(LOG_LEVEL_DEBUG, kpriv->log_level, "         prediction tree : \n%s", pstr);
        free(pstr);

        cur_faces++;

        if (cur_faces == kpriv->objs_detection_max) {
          LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "      reached max limit of faces to add to metadata");
          break;
        }
      }
    }
    /*
    predictions[i] = parent_predict; // overwrite old one appended(updated) with new things
    */
  }
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "end run");

  return true;
}

int vvas_xfacedetectrecog::requiredwidth(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  // return 720;
  return model_fd->getInputWidth();
}

int vvas_xfacedetectrecog::requiredheight(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  // return 1280;
  return model_fd->getInputHeight();
}

int vvas_xfacedetectrecog::supportedbatchsz(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return model_fd->get_input_batch();
}

int vvas_xfacedetectrecog::close(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return true;
}

vvas_xfacedetectrecog::~vvas_xfacedetectrecog() {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
}