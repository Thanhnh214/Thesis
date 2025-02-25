-- Copyright 2016 The Cartographer Authors
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--      http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "imu_link", -- imu_link, If you are using gazebo, use 'base_footprint' (libgazebo_ros_imu's bug)
  published_frame = "base_footprint",
  odom_frame = "odom",
  provide_odom_frame = true,
  publish_frame_projected_to_2d = true,
  use_odometry = true,
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 1,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 0,
  lookup_transform_timeout_sec = 0.2,
  submap_publish_period_sec = 0.3,
  pose_publish_period_sec = 5e-3,
  publish_to_tf = true,
  publish_tracked_pose = true,
  trajectory_publish_period_sec = 30e-3,
  rangefinder_sampling_ratio = 1.,
  odometry_sampling_ratio = 1.,
  fixed_frame_pose_sampling_ratio = 1.,
  imu_sampling_ratio = 1.,
  landmarks_sampling_ratio = 1.,
}

MAP_BUILDER.use_trajectory_builder_2d = true
TRAJECTORY_BUILDER_2D.min_range = 0.2
TRAJECTORY_BUILDER_2D.use_imu_data = false

-----------------TUNE THESE PARAMETERS FOR BIAS TO ODOMETRY-------------------------------

TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight = 5
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.rotation_weight = 10

POSE_GRAPH.constraint_builder.loop_closure_translation_weight = 50
POSE_GRAPH.constraint_builder.loop_closure_rotation_weight = 10

POSE_GRAPH.optimization_problem.local_slam_pose_translation_weight = 100
POSE_GRAPH.optimization_problem.local_slam_pose_rotation_weight = 10
POSE_GRAPH.optimization_problem.odometry_translation_weight = 1000
POSE_GRAPH.optimization_problem.odometry_rotation_weight = 500

-----------------TUNE THESE PARAMETERS FOR LOW LATENCY-------------------------------

------------Global SLAM------------
POSE_GRAPH.optimize_every_n_nodes = 100 -- Decrease
POSE_GRAPH.global_sampling_ratio = 0.01 -- Decrease
POSE_GRAPH.constraint_builder.sampling_ratio = 0.5 -- Decrease
POSE_GRAPH.constraint_builder.min_score = 0.85 -- Increase
POSE_GRAPH.global_constraint_search_after_n_seconds = 10 -- Increase

---------Global/Local SLAM---------
TRAJECTORY_BUILDER_2D.submaps.num_range_data = 720 -- Decrease
TRAJECTORY_BUILDER_2D.max_range = 5. -- Decrease

-------------------------------------------------------------------------------------

return options