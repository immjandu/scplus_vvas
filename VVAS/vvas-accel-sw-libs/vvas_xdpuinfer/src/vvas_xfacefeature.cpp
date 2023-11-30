/*
 * Copyright (C) 2022 Xilinx, Inc.
 * Copyright (C) 2022-2023 Advanced Micro Devices, Inc.
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

#include "vvas_xfacefeature.hpp"

vvas_xfacefeature::vvas_xfacefeature (vvas_xkpriv * kpriv,
    const std::string & model_name, bool need_preprocess)
{
  // VvasDpuInferPrivate *kpriv = (VvasDpuInferPrivate *)handle;
  log_level = kpriv->log_level;
  LOG_MESSAGE (LOG_LEVEL_DEBUG, kpriv->log_level, "enter");

  model = vitis::ai::FaceFeature::create (model_name, need_preprocess);
}

int
vvas_xfacefeature::run (vvas_xkpriv * kpriv, std::vector < cv::Mat > &images,
    GstInferencePrediction ** predictions)
{
  std::vector < vitis::ai::FaceFeatureFloatResult > results;
  // std::vector < vitis::ai::FaceFeatureFixedResult > results; 

  LOG_MESSAGE (LOG_LEVEL_DEBUG, kpriv->log_level, "before run");

  results = model->run (images);
  // results = model->run_fixed (images);
  
  for (auto i = 0u; i < results.size(); i++) {
    GstInferencePrediction *parent_predict = NULL;
    BoundingBox parent_bbox;
    parent_predict = predictions[i];
    int cols = images[i].cols;
    int rows = images[i].rows;
    if (!parent_predict) {
      parent_bbox.x = parent_bbox.y = 0;
      parent_bbox.width = cols;
      parent_bbox.height = rows;
      parent_predict = gst_inference_prediction_new_full(&parent_bbox);
    }

    FaceFeature *feat;
    GstInferencePrediction *predict;
    predict = gst_inference_prediction_new();
    char *pstr; /* prediction string */

    feat = &predict->feature;
    memcpy((void *) &feat->feature, (void *) &(*results[i].feature)[0], 512 * sizeof(float));

    if ((LOG_LEVEL_INFO <= kpriv->log_level)) {
      LOG_MESSAGE (LOG_LEVEL_INFO, kpriv->log_level, "float_features:");
      for (int j = 0; j < 512; j++)
        printf (" %f ", feat->feature[j]);
      printf ("\n");
    }

    /* add class and name in prediction node */
    // predict.model_class = (VvasClass) kpriv->modelclass;
    // predict.model_name = strdup (kpriv->modelname.c_str ());
    gst_inference_prediction_append(parent_predict, predict);

    pstr = gst_inference_prediction_to_string(parent_predict);
    LOG_MESSAGE (LOG_LEVEL_DEBUG, kpriv->log_level, "prediction tree : \n%s", pstr);
    free (pstr);

    predictions[i] = parent_predict;

  }

  return true;
}


int vvas_xfacefeature::requiredwidth (void)
{
  LOG_MESSAGE (LOG_LEVEL_DEBUG, log_level, "enter");
  return model->getInputWidth ();
}

int vvas_xfacefeature::requiredheight (void)
{
  LOG_MESSAGE (LOG_LEVEL_DEBUG, log_level, "enter");
  return model->getInputHeight ();
}

int vvas_xfacefeature::supportedbatchsz (void)
{
  LOG_MESSAGE (LOG_LEVEL_DEBUG, log_level, "enter");
  return model->get_input_batch ();
}

int vvas_xfacefeature::close (void)
{
  LOG_MESSAGE (LOG_LEVEL_DEBUG, log_level, "enter");
  return true;
}

vvas_xfacefeature::~vvas_xfacefeature ()
{
  LOG_MESSAGE (LOG_LEVEL_DEBUG, log_level, "enter");
}