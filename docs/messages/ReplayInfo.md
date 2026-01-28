# ReplayInfo

**Message Type**: `morai_msgs/msg/ReplayInfo`

## Message Definition

```
std_msgs/Header header

float64 ego_acc
float64 ego_brake
float64 ego_steer

geometry_msgs/Quaternion orientation

geometry_msgs/Vector3 linear_acceleration

geometry_msgs/Vector3 angular_velocity

int32 num_of_npcs
int32 num_of_pedestrian
int32 num_of_obstacle

ObjectStatus[] npc_list 

ObjectStatus[] pedestrian_list

ObjectStatus[] obstacle_list ```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `ego_acc` | `float64` | - |
| `ego_brake` | `float64` | - |
| `ego_steer` | `float64` | - |
| `orientation` | `geometry_msgs/Quaternion` | - |
| `linear_acceleration` | `geometry_msgs/Vector3` | - |
| `angular_velocity` | `geometry_msgs/Vector3` | - |
| `num_of_npcs` | `int32` | - |
| `num_of_pedestrian` | `int32` | - |
| `num_of_obstacle` | `int32` | - |
| `npc_list` | `ObjectStatus[]` | - |
| `pedestrian_list` | `ObjectStatus[]` | - |
| `obstacle_list` | `ObjectStatus[]` | - |

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

