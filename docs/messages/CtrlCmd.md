# CtrlCmd

**Message Type**: `morai_msgs/msg/CtrlCmd`

Control command signals for steering, moving, and stopping the ego vehicle.

**Topic**: `/ctrl_cmd`

## Message Definition

```
# CtrlCmd
# Control command signals for steering, moving, and stopping the ego vehicle.
# Topic: /ctrl_cmd

std_msgs/Header header

int32 longl_cmd_type  # Control method index (1: Throttle, 2: Velocity, 3: Acceleration)

float64 accel  # Accelerator pedal input, range 0~1
float64 brake  # Brake pedal input, range 0~1
float64 front_steer  # Front wheel steer angle [rad]
float64 rear_steer  # Rear wheel steer angle [rad]

float64 velocity  # Target velocity, active when longl_cmd_type == 2 [km/h]
float64 acceleration  # Target acceleration, active when longl_cmd_type == 3 [m/s^2]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `longl_cmd_type` | `int32` | Control method index (1: Throttle, 2: Velocity, 3: Acceleration) |
| `accel` | `float64` | Accelerator pedal input, range 0~1 |
| `brake` | `float64` | Brake pedal input, range 0~1 |
| `front_steer` | `float64` | Front wheel steer angle [rad] |
| `rear_steer` | `float64` | Rear wheel steer angle [rad] |
| `velocity` | `float64` | Target velocity, active when longl_cmd_type == 2 [km/h] |
| `acceleration` | `float64` | Target acceleration, active when longl_cmd_type == 3 [m/s^2] |

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

