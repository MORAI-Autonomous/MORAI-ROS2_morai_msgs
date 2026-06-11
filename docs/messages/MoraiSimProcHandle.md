# MoraiSimProcHandle

**Message Type**: `morai_msgs/msg/MoraiSimProcHandle`

Playback commands and conditions for rosbag replay.

## Message Definition

```
# MoraiSimProcHandle
# Playback commands and conditions for rosbag replay.

std_msgs/Header header

uint8 sim_process_status  # Process status (1: Playing, 2: Paused, 32: Stopped)

int16 replay_option  # Bitmask (1: load file, 2: designate target, 4: set start time, 8: set speed)
string rosbag_file_name  # Filename of the rosbag file to load
int16 replay_target_option  # Bitmask (1: ego vehicle, 2: NPC vehicle, 4: pedestrian)

int32 replay_speed  # Playback speed multiplier (e.g., 1, 2)
int32 start_time  # Start time [ms]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `sim_process_status` | `uint8` | Process status (1: Playing, 2: Paused, 32: Stopped) |
| `replay_option` | `int16` | Bitmask (1: load file, 2: designate target, 4: set start time, 8: set speed) |
| `rosbag_file_name` | `string` | Filename of the rosbag file to load |
| `replay_target_option` | `int16` | Bitmask (1: ego vehicle, 2: NPC vehicle, 4: pedestrian) |
| `replay_speed` | `int32` | Playback speed multiplier (e.g., 1, 2) |
| `start_time` | `int32` | Start time [ms] |

## Usage Example

### Python

```python
from morai_msgs.msg import MoraiSimProcHandle

# Create message
msg = MoraiSimProcHandle()
msg.header = ''
msg.sim_process_status = 0
msg.replay_option = 0
```

### C++

```cpp
#include <morai_msgs/msg/moraisimprochandle.hpp>

// Create message
auto msg = morai_msgs::msg::MoraiSimProcHandle();
msg.header = "";
msg.sim_process_status = 0;
msg.replay_option = 0;
```

