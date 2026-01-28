# MoraiSimProcStatus

**Message Type**: `morai_msgs/msg/MoraiSimProcStatus`

## Message Definition

```
std_msgs/Header header

builtin_interfaces/Time latest_command_time
uint8 command_result
uint8 current_mode
uint8 current_status

```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `latest_command_time` | `builtin_interfaces/Time` | - |
| `command_result` | `uint8` | - |
| `current_mode` | `uint8` | - |
| `current_status` | `uint8` | - |

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

