# GhostCmd

**Message Type**: `morai_msgs/msg/GhostCmd`

## Message Definition

```
std_msgs/Header header

geometry_msgs/Vector3 position
geometry_msgs/Vector3 rotation

float64 velocity
float64 steer_angle
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `position` | `geometry_msgs/Vector3` | - |
| `rotation` | `geometry_msgs/Vector3` | - |
| `velocity` | `float64` | - |
| `steer_angle` | `float64` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import GhostCmd

# Create message
msg = GhostCmd()
msg.header = ''
msg.position = ''
msg.rotation = ''
```

### C++

```cpp
#include <morai_msgs/msg/ghostcmd.hpp>

// Create message
auto msg = morai_msgs::msg::GhostCmd();
msg.header = "";
msg.position = "";
msg.rotation = "";
```

