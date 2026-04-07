# MoraiSimProcHandle

**Message Type**: `morai_msgs/msg/MoraiSimProcHandle`

## Message Definition

```
std_msgs/Header header

uint8 sim_process_status

int16 replay_option
string rosbag_file_name
int16 replay_target_option

int32 replay_speed
int32 start_time
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `sim_process_status` | `uint8` | - |
| `replay_option` | `int16` | - |
| `rosbag_file_name` | `string` | - |
| `replay_target_option` | `int16` | - |
| `replay_speed` | `int32` | - |
| `start_time` | `int32` | - |

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

