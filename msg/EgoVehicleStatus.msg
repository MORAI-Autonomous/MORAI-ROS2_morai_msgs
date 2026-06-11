# EgoVehicleStatus
# Status telemetry of the ego vehicle for closed-loop control.
# Topic: /Ego_topic

std_msgs/Header header
int32 unique_id  # Object unique id
geometry_msgs/Vector3 acceleration  # Acceleration vector [m/s^2]
geometry_msgs/Vector3 position  # Current position in ENU coordinates [m]
geometry_msgs/Vector3 velocity  # Velocity vector [m/s]
geometry_msgs/Vector3 angular_velocity  # Angular velocity [deg/s]

float64 heading  # Vehicle heading [deg]
float64 accel  # Accelerator pedal, range 0~1
float64 brake  # Brake pedal, range 0~1
float64 front_steer  # Front wheel angle [deg]
float64 rear_steer  # Rear wheel angle [deg]

float32 tire_lateral_force_fl  # Front-left tire lateral force
float32 tire_lateral_force_fr  # Front-right tire lateral force
float32 tire_lateral_force_rl  # Rear-left tire lateral force
float32 tire_lateral_force_rr  # Rear-right tire lateral force

float32 side_slip_angle_fl  # Front-left side slip angle
float32 side_slip_angle_fr  # Front-right side slip angle
float32 side_slip_angle_rl  # Rear-left side slip angle
float32 side_slip_angle_rr  # Rear-right side slip angle

float32 tire_cornering_stiffness_fl  # Front-left cornering stiffness
float32 tire_cornering_stiffness_fr  # Front-right cornering stiffness
float32 tire_cornering_stiffness_rl  # Rear-left cornering stiffness
float32 tire_cornering_stiffness_rr  # Rear-right cornering stiffness

float32 distance_left_lane_boundary  # Distance from left lane boundary [m]
float32 distance_right_lane_boundary  # Distance from right lane boundary [m]
float32 cross_track_error  # Distance from lane center, right-positive [m]
