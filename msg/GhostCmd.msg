# GhostCmd
# Re-simulation (ghost) control of the ego vehicle using recorded data.
# Topic: /ghost_ctrl_cmd

std_msgs/Header header

geometry_msgs/Vector3 position  # Ego vehicle position (X, Y, Z) [m]
geometry_msgs/Vector3 rotation  # Ego vehicle rotation (Roll, Pitch, Yaw) [deg]

float64 velocity  # Speed of the ego vehicle [km/h]
float64 steer_angle  # Front wheel steer angle [deg]
