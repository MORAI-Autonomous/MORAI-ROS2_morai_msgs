# EventInfo
# One-time event control for vehicle state changes (used by the EventCmd service).
# Service: /Service_MoraiEventCmd (request/response)

std_msgs/Header header

int8 option  # Bitmask for fields to apply (1: ctrl_mode, 2: gear, 4: lamps, 8: set_pause)
int32 ctrl_mode  # Control mode (1: Keyboard, 2: Gamepad, 3: External, 6: Auto agent controlled)
int32 gear  # Gear selection (-1: No change, 1: Parking, 2: Reverse, 3: Neutral, 4: Drive)
Lamps lamps  # Vehicle lamp controls
bool set_pause  # true: pause simulation, false: continue
