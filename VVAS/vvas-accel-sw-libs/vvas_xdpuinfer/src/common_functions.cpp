#include <algorithm>
#include <cnpy.h>
#include <iostream>
#include "common_functions.hpp"

bool compare_bbox_by_area(const vitis::ai::FaceDetectResult::BoundingBox &box1, const vitis::ai::FaceDetectResult::BoundingBox &box2) {
  float area1 = (box1.width * box1.height);
  float area2 = (box2.width * box2.height);
  return (area1 > area2);
}

std::tuple<float, int> get_max_values(std::array<float, 512> arr, int len) {
  auto max_obj = std::max_element(arr.begin(), arr.begin() + len + 1);
  float max_val = *max_obj;
  int max_idx = std::distance(arr.begin(), max_obj);

  return std::make_tuple(max_val, max_idx);
}

std::tuple<float, int> get_max_values_old(std::array<float, 512> arr, int len) {
  float max_val = -1.0; // max_it
  int max_idx = 0; // argmax
  int idx = 0;

  for (const float f : arr) {
    if (idx >= len)
      break;
    else {
      if (f > max_val) {
        max_val = f;
        max_idx = idx;
      }
      idx++;
    }
  }

  return std::make_tuple(max_val, max_idx);
}

float feature_norm(const float *feature) {
  float sum = 0;
  for (int i = 0; i < 512; ++i) {
    sum += feature[i] * feature[i];
  }
  return 1.f / sqrt(sum);
}

float feature_dot(const float *f1, const float *f2) {
  float dot = 0;
  for (int i = 0; i < 512; ++i) {
    dot += f1[i] * f2[i];
  }
  return (float)dot;
}

float cosine_similarity(const float *feature1, const float *feature2) {
  float norm1 = feature_norm(feature1);
  float norm2 = feature_norm(feature2);
  return feature_dot(feature1, feature2) * norm1 * norm2;
}

float score_map(float score) { return 1.0 / (1 + exp(-12.4 * score + 3.763)); }

std::tuple<std::vector<std::vector<float>>, std::vector<float>, std::vector<std::string>> load_embeddings(std::string embeddings_npzpath) {

  // std::map<std::string, std::vector<float>> embeddings_map;
  cnpy::npz_t npy_map = cnpy::npz_load(embeddings_npzpath); // using npz_t = std::map<std::string, NpyArray>;

  std::vector<std::vector<float>> embedding_arr;
  std::vector<float> embedding_norm_arr;
  std::vector<std::string> embedding_class_arr;

  for (auto &pair : npy_map) {
    std::string fname = pair.first;
    cnpy::NpyArray value_arr = pair.second;
    int value_size = value_arr.num_vals; // 512

    const float* value_ptr = value_arr.data<float>();
    std::vector<float> value(value_ptr, value_ptr + value_size);
    embedding_arr.push_back(value);
    embedding_norm_arr.push_back(feature_norm(value_ptr));
    embedding_class_arr.push_back(fname.substr(0, fname.rfind('/')));
  }
  // embedding_arr : {[e0,e1, ..., e512],[e0,e1, ..., e512], ...}
  // embedding_norm_arr : {e0, e1, ...}
  // embedding_class_arr : {c1, c1, ...} // c1 like "{class_name}/{fname}"
  return std::make_tuple(embedding_arr, embedding_norm_arr, embedding_class_arr);
}

std::vector<std::string> get_label_array(vvas_xkpriv * kpriv) {
  std::vector<std::string> label_arr;
  for (int i=0; i < kpriv->num_labels; i++)
    label_arr.push_back(kpriv->labelptr[i].name);
  return label_arr;
}