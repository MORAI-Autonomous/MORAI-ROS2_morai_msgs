# CtrlCmd

**Message Type**: `morai_msgs/msg/CtrlCmd`

## Message Definition

```
std_msgs/Header header

int32 longl_cmd_type

float64 accel
float64 brake
float64 front_steer
float64 rear_steer

float64 velocity
float64 acceleration
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `longl_cmd_type` | `int32` | - |
| `accel` | `float64` | - |
| `brake` | `float64` | - |
| `front_steer` | `float64` | - |
| `rear_steer` | `float64` | - |
| `velocity` | `float64` | - |
| `acceleration` | `float64` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import CtrlCmd

# Create message
msg = CtrlCmd()
msg.header = ''
msg.longl_cmd_type = 0
msg.accel = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/ctrlcmd.hpp>

// Create message
auto msg = morai_msgs::msg::CtrlCmd();
msg.header = "";
msg.longl_cmd_type = 0;
msg.accel = 0.0;
```

