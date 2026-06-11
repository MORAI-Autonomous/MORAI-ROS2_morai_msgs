# SetTrafficLight
# Control command to change a specific traffic light state.
# Topic: /SetTrafficLight

std_msgs/Header header

string traffic_light_index  # Unique index of the traffic light
int16 traffic_light_status  # Target state (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit)
