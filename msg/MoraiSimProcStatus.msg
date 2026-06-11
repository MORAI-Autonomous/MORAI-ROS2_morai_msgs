# MoraiSimProcStatus
# Current status of the simulator replay system.

std_msgs/Header header

builtin_interfaces/Time latest_command_time  # Timestamp of last MoraiSimProcHandle received (0 if never received)
uint8 command_result  # Result (0: initial, 1: success, 16: failed, 32: rosbag load failed, 48: loaded but failed)
uint8 current_mode  # Simulator mode (1: simulation, 16: replay)
uint8 current_status  # Simulator status (1: running, 16: paused, 32: paused at end of rosbag)
