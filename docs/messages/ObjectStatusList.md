# ObjectStatusList

**Message Type**: `morai_msgs/msg/ObjectStatusList`

Details of the closest objects around the ego vehicle (NPCs, pedestrians, obstacles).

**Topic**: `/Object_topic`

## Message Definition

```
# ObjectStatusList
# Details of the closest objects around the ego vehicle (NPCs, pedestrians, obstacles).
# Topic: /Object_topic

std_msgs/Header header

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
| `num_of_npcs` | `int32` | Number of NPC vehicles |
| `num_of_pedestrian` | `int32` | Number of pedestrians |
| `num_of_obstacle` | `int32` | Number of static obstacles |
| `npc_list` | `ObjectStatus[]` | NPC vehicle information |
| `pedestrian_list` | `ObjectStatus[]` | Pedestrian information |
| `obstacle_list` | `ObjectStatus[]` | Obstacle information |

## Usage Example

### Python

```python
from morai_msgs.msg import ObjectStatusList

# Create message
msg = ObjectStatusList()
msg.header = ''
msg.num_of_npcs = 0
msg.num_of_pedestrian = 0
```

### C++

```cpp
#include <morai_msgs/msg/objectstatuslist.hpp>

// Create message
auto msg = morai_msgs::msg::ObjectStatusList();
msg.header = "";
msg.num_of_npcs = 0;
msg.num_of_pedestrian = 0;
```

