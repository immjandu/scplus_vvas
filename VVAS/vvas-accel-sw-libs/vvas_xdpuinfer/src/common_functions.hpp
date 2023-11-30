#pragma once
#include <vitis/ai/facedetect.hpp>
#include "vvas_xdpupriv.hpp"

bool compare_bbox_by_area(const vitis::ai::FaceDetectResult::BoundingBox &box1, const vitis::ai::FaceDetectResult::BoundingBox &box2);

std::tuple<float, int> get_max_values(std::array<float, 512> arr, int len);

std::tuple<float, int> get_max_values_old(std::array<float, 512> arr, int len);

float feature_norm(const float *feature);

float feature_dot(const float *f1, const float *f2);

float cosine_similarity(const float *feature, const float *feature_lib);

float score_map(float score);

std::tuple<std::vector<std::vector<float>>, std::vector<float>, std::vector<std::string>> load_embeddings(std::string embeddings_npzpath);

std::vector<std::string> get_label_array(vvas_xkpriv * kpriv);