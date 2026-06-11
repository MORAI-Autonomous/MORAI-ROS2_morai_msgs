# GhostCmd

**Message Type**: `morai_msgs/msg/GhostCmd`

Re-simulation (ghost) control of the ego vehicle using recorded data.

**Topic**: `/ghost_ctrl_cmd`

## Message Definition

```
# GhostCmd
# Re-simulation (ghost) control of the ego vehicle using recorded data.
# Topic: /ghost_ctrl_cmd

std_msgs/Header header

geometry_msgs/Vector3 position  # Ego vehicle position (X, Y, Z) [m]
geometry_msgs/Vector3 rotation  # Ego vehicle rotation (Roll, Pitch, Yaw) [deg]

float64 velocity  # Speed of the ego vehicle [km/h]
float64 steer_angle  # Front wheel steer angle [deg]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `position` | `geometry_msgs/Vector3` | Ego vehicle position (X, Y, Z) [m] |
| `rotation` | `geometry_msgs/Vector3` | Ego vehicle rotation (Roll, Pitch, Yaw) [deg] |
| `velocity` | `float64` | Speed of the ego vehicle [km/h] |
| `steer_angle` | `float64` | Front wheel steer angle [deg] |

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

