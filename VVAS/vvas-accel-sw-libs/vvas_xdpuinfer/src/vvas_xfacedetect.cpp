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
#include "common_functions.hpp"

vvas_xfacedetect::vvas_xfacedetect(vvas_xkpriv * kpriv, const std::string & model_name, bool need_preprocess) {
  log_level = kpriv->log_level;
  LOG_MESSAGE(LOG_LEVEL_INFO, log_level, "enter : create model");
  model = vitis::ai::FaceDetect::create(model_name, need_preprocess);
}

int vvas_xfacedetect::run(vvas_xkpriv * kpriv, std::vector<cv::Mat>& images, GstInferencePrediction **predictions) {
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "run : %d x %d", images[0].rows, images[0].cols);

  auto results = model->run(images);
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "size of results = %d", results.size());
  char *pstr; // prediction string

  if (kpriv->objs_detection_max > 0) {
    // LOG_MESSAGE(LOG_LEVEL_DEBUG, kpriv->log_level, "sort detected faces based on bbox area");
    /* sort objects based on dimension to pick objects with bigger bbox */
    for (unsigned int i = 0u; i < results.size(); i++) {
      std::sort(results[i].rects.begin(), results[i].rects.end(), compare_bbox_by_area);
    }
  } else {
    LOG_MESSAGE(LOG_LEVEL_WARNING, kpriv->log_level, "max-objects count is zero. So, not doing any metadata processing");
    return true;
  }

  for (auto i = 0u; i < results.size(); i++) {
    GstInferencePrediction *parent_predict = NULL;
    unsigned int cur_faces = 0;

    if (results[i].rects.size()) {
      BoundingBox parent_bbox;
      int cols = images[i].cols;
      int rows = images[i].rows;

      parent_predict = predictions[i];
      LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "   results[%d]rects size : %ld", i, results[i].rects.size());
      for (auto & r: results[i].rects) {

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
        float confidence = r.score;

        BoundingBox bbox;
        GstInferencePrediction *predict;
        GstInferenceClassification *c = NULL;

        bbox.x = xmin;
        bbox.y = ymin;
        bbox.width = xmax - xmin;
        bbox.height = ymax - ymin;
        predict = gst_inference_prediction_new_full(&bbox);
        c = gst_inference_classification_new_full(-1, confidence, NULL, 0, NULL, NULL, NULL);
        gst_inference_prediction_append_classification(predict, c);
        gst_inference_prediction_append(parent_predict, predict);

        LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "      DETECTED: %f %f %f %f (%f)", xmin, ymin, xmax, ymax, confidence);

        cur_faces++;

        if (cur_faces == kpriv->objs_detection_max) {
          LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "      reached max limit of faces to add to metadata");
          break;
        }
      }

      if (parent_predict) {
        pstr = gst_inference_prediction_to_string(parent_predict);
        LOG_MESSAGE(LOG_LEVEL_DEBUG, kpriv->log_level, "   FD prediction tree : \n%s", pstr);
        free(pstr);
      }
    }
    predictions[i] = parent_predict;

  }
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "end run");

  return true;
}


int vvas_xfacedetect::requiredwidth(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return model->getInputWidth();
}

int vvas_xfacedetect::requiredheight(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return model->getInputHeight();
}

int vvas_xfacedetect::supportedbatchsz(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return model->get_input_batch();
}

int vvas_xfacedetect::close(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return true;
}

vvas_xfacedetect::~vvas_xfacedetect() {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
}