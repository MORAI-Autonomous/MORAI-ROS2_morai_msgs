# CtrlCmd
# Control command signals for steering, moving, and stopping the ego vehicle.
# Topic: /ctrl_cmd

std_msgs/Header header

int32 longl_cmd_type  # Control method index (1: Throttle, 2: Velocity, 3: Acceleration)

float64 accel  # Accelerator pedal input, range 0~1
float64 brake  # Brake pedal input, range 0~1
float64 front_steer  # Front wheel steer angle [rad]
float64 rear_steer  # Rear wheel steer angle [rad]

float64 velocity  # Target velocity, active when longl_cmd_type == 2 [km/h]
float64 acceleration  # Target acceleration, active when longl_cmd_type == 3 [m/s^2]
