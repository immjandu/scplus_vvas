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

#include "vvas_xfacerecog.hpp"
#include "common_functions.hpp"
#include <algorithm>

vvas_xfacerecog::vvas_xfacerecog(vvas_xkpriv * kpriv, const std::string & model_name, bool need_preprocess) {
  log_level = kpriv->log_level;
  LOG_MESSAGE(LOG_LEVEL_INFO, log_level, "enter : create model");
  model = vitis::ai::FaceFeature::create(model_name, need_preprocess);
  LOG_MESSAGE(LOG_LEVEL_INFO, log_level, "enter : %s", kpriv->embeddings_npzpath.c_str());
  std::tie(embedding_arr, embedding_norm_arr, embedding_class_arr) = load_embeddings(kpriv->embeddings_npzpath);
  label_arr = get_label_array(kpriv);
}

int vvas_xfacerecog::run(vvas_xkpriv * kpriv, std::vector<cv::Mat>& images, GstInferencePrediction **predictions) {
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "run : %d x %d", images[0].rows, images[0].cols);
  char *pstr;

  for (auto i=0; i < images.size(); i++) {
    // if (kpriv->log_level==LOG_LEVEL_DEBUG) {
    //   pstr = gst_inference_prediction_to_string(predictions[i]);
    //   LOG_MESSAGE(LOG_LEVEL_DEBUG, kpriv->log_level, "init_FR parent_predict(=prediction[%d]) tree : \n%s", i, pstr);
    // }

    // crop face
    BoundingBox bbox = predictions[i]->bbox;
    // LOG_MESSAGE (LOG_LEVEL_INFO, kpriv->log_level, "FR crop [%d] : %dx%d -> %dx%d(%dx%d)\n", i, images[i].rows, images[i].cols, bbox.x, bbox.y, bbox.width, bbox.height);
    cv::Mat cropped_img = images[i](Range(bbox.y, bbox.y + bbox.height), Range(bbox.x, bbox.x + bbox.width));

    // init parent_bbox, parent_predict
    GstInferencePrediction *parent_predict = predictions[i];
    BoundingBox parent_bbox;
    parent_bbox.x = parent_bbox.y = 0;
    parent_bbox.width = parent_bbox.height = 0;
    parent_predict->bbox = parent_bbox;

    // resize face
    //cv::Mat resized_img;
    //cv::resize(cropped_img, resized_img, cv::Size(160, 160), INTER_LINEAR);
    //cv::imwrite("fr/resized_img_" + std::to_string(bbox.x) + "_" + std::to_string(bbox.y) + ".png", resized_img);

    auto result = model->run(cropped_img);
    float max_val = -1.0;
    int max_idx = 0;
    // std::tie(max_val, max_idx) = get_max_values(*result.feature, kpriv->num_labels);
    // LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "         RECOG feature max idx and value : %d / (%f)", max_idx, max_val);

    float embedding_max_val = -1.0;
    int embedding_max_idx = 0;
    for (int i=0; i<embedding_arr.size(); i++) {
      float feature1_norm = feature_norm((*result.feature).data());
      float feature2_norm = embedding_norm_arr[i];
      float dot = feature_dot((*result.feature).data(), embedding_arr[i].data());
      float cosine_sim = dot * feature1_norm * feature2_norm;
      if (cosine_sim > embedding_max_val) {
        embedding_max_val = cosine_sim;
        embedding_max_idx = i;
      }
    }
    std::string max_class = embedding_class_arr[embedding_max_idx];
    max_idx = std::find(label_arr.begin(), label_arr.end(), max_class) - label_arr.begin();
    max_val = embedding_max_val;
    LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "         RECOG feature max idx and value : %d / %s (%f)", max_idx, max_class.c_str(), max_val);

    GstInferencePrediction * predict = gst_inference_prediction_new_full(&bbox);
    // add(append) classification info
    string label_display_name = kpriv->labelptr[max_idx].display_name;
    const char* label_display_name_char = label_display_name.c_str();
    LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "RECOGNIZED! idx=%d, label=%s, value=%f", max_idx, label_display_name_char, max_val);
    GstInferenceClassification * c = gst_inference_classification_new_full(max_idx, max_val, label_display_name_char, kpriv->num_labels, NULL, NULL, NULL);
    gst_inference_prediction_append_classification(predict, c);
    gst_inference_prediction_append(parent_predict, predict);

    pstr = gst_inference_prediction_to_string(parent_predict);
    LOG_MESSAGE(LOG_LEVEL_DEBUG, kpriv->log_level, "FR parent_predict tree : \n%s", pstr);

    predictions[i] = parent_predict; // overwrite old one appended(updated) with new things

  }
  LOG_MESSAGE(LOG_LEVEL_INFO, kpriv->log_level, "end run");
  free(pstr);
  return true;
}

int vvas_xfacerecog::requiredwidth(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  // return model->getInputWidth();
  return 1280; // raw video size 1280
}

int vvas_xfacerecog::requiredheight(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  // return model->getInputHeight();
  return 720; // raw video size 720
}

int vvas_xfacerecog::supportedbatchsz(void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return model->get_input_batch();
}

int vvas_xfacerecog::close (void) {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
  return true;
}

vvas_xfacerecog::~vvas_xfacerecog() {
  LOG_MESSAGE(LOG_LEVEL_DEBUG, log_level, "enter");
}