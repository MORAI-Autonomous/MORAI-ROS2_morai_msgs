# ReplayInfo

**Message Type**: `morai_msgs/msg/ReplayInfo`

Replay data containing ego vehicle state and surrounding object information.

**Topic**: `/ReplayInfo_topic`

## Message Definition

```
# ReplayInfo
# Replay data containing ego vehicle state and surrounding object information.
# Topic: /ReplayInfo_topic

std_msgs/Header header

float64 ego_acc  # Accelerator pedal, range 0~1
float64 ego_brake  # Brake pedal, range 0~1
float64 ego_steer  # Front wheel angle [deg]

geometry_msgs/Quaternion orientation  # Current orientation

geometry_msgs/Vector3 linear_acceleration  # Current linear acceleration

geometry_msgs/Vector3 angular_velocity  # Current angular velocity

int32 num_of_npcs  # Number of NPC vehicles
int32 num_of_pedestrian  # Number of pedestrians
int32 num_of_obstacle  # Number of static obstacles

ObjectStatus[] npc_list  # NPC vehicle information

ObjectStatus[] pedestrian_list  # Pedestrian information

ObjectStatus[] obstacle_list  # Obstacle information
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `ego_acc` | `float64` | Accelerator pedal, range 0~1 |
| `ego_brake` | `float64` | Brake pedal, range 0~1 |
| `ego_steer` | `float64` | Front wheel angle [deg] |
| `orientation` | `geometry_msgs/Quaternion` | Current orientation |
| `linear_acceleration` | `geometry_msgs/Vector3` | Current linear acceleration |
| `angular_velocity` | `geometry_msgs/Vector3` | Current angular velocity |
| `num_of_npcs` | `int32` | Number of NPC vehicles |
| `num_of_pedestrian` | `int32` | Number of pedestrians |
| `num_of_obstacle` | `int32` | Number of static obstacles |
| `npc_list` | `ObjectStatus[]` | NPC vehicle information |
| `pedestrian_list` | `ObjectStatus[]` | Pedestrian information |
| `obstacle_list` | `ObjectStatus[]` | Obstacle information |

## Usage Example

### Python

```python
from morai_msgs.msg import ReplayInfo

# Create message
msg = ReplayInfo()
msg.header = ''
msg.ego_acc = 0.0
msg.ego_brake = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/replayinfo.hpp>

// Create message
auto msg = morai_msgs::msg::ReplayInfo();
msg.header = "";
msg.ego_acc = 0.0;
msg.ego_brake = 0.0;
```

