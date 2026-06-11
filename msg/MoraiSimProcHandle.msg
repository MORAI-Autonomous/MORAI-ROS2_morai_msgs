# MoraiSimProcHandle
# Playback commands and conditions for rosbag replay.

std_msgs/Header header

uint8 sim_process_status  # Process status (1: Playing, 2: Paused, 32: Stopped)

int16 replay_option  # Bitmask (1: load file, 2: designate target, 4: set start time, 8: set speed)
string rosbag_file_name  # Filename of the rosbag file to load
int16 replay_target_option  # Bitmask (1: ego vehicle, 2: NPC vehicle, 4: pedestrian)

int32 replay_speed  # Playback speed multiplier (e.g., 1, 2)
int32 start_time  # Start time [ms]
