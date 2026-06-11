# MoraiSimProcStatus

**Message Type**: `morai_msgs/msg/MoraiSimProcStatus`

Current status of the simulator replay system.

## Message Definition

```
# MoraiSimProcStatus
# Current status of the simulator replay system.

std_msgs/Header header

builtin_interfaces/Time latest_command_time  # Timestamp of last MoraiSimProcHandle received (0 if never received)
uint8 command_result  # Result (0: initial, 1: success, 16: failed, 32: rosbag load failed, 48: loaded but failed)
uint8 current_mode  # Simulator mode (1: simulation, 16: replay)
uint8 current_status  # Simulator status (1: running, 16: paused, 32: paused at end of rosbag)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `latest_command_time` | `builtin_interfaces/Time` | Timestamp of last MoraiSimProcHandle received (0 if never received) |
| `command_result` | `uint8` | Result (0: initial, 1: success, 16: failed, 32: rosbag load failed, 48: loaded but failed) |
| `current_mode` | `uint8` | Simulator mode (1: simulation, 16: replay) |
| `current_status` | `uint8` | Simulator status (1: running, 16: paused, 32: paused at end of rosbag) |

## Usage Example

### Python

```python
from morai_msgs.msg import MoraiSimProcStatus

# Create message
msg = MoraiSimProcStatus()
msg.header = ''
msg.latest_command_time = 0
msg.command_result = 0
```

### C++

```cpp
#include <morai_msgs/msg/moraisimprocstatus.hpp>

// Create message
auto msg = morai_msgs::msg::MoraiSimProcStatus();
msg.header = "";
msg.latest_command_time = 0;
msg.command_result = 0;
```

