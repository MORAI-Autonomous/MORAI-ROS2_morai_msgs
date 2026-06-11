# MultiEgoSetting
# Control multiple ego vehicles in the scene with external controllers.
# Topic: /ego_setting

std_msgs/Header header

int32 number_of_ego_vehicle  # Number of multi-ego vehicles
int32 camera_index  # Unique index of the viewed vehicle
int32[] ego_index  # Unique indices of multi-ego vehicles to control

float64[] global_position_x  # X-axis position of each multi-ego
float64[] global_position_y  # Y-axis position of each multi-ego
float64[] global_position_z  # Z-axis position (elevation) of each multi-ego
float32[] global_roll  # Roll angle of each multi-ego
float32[] global_pitch  # Pitch angle of each multi-ego
float32[] global_yaw  # Heading (yaw) angle of each multi-ego
float32[] velocity  # Velocity of each multi-ego
int8[] gear  # Gear of each multi-ego (1: Parking, 2: Reverse, 3: Neutral, 4: Drive)
int8[] ctrl_mode  # Control mode of each multi-ego (1: keyboard, 16: auto)
