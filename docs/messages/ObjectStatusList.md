# ObjectStatusList

**Message Type**: `morai_msgs/msg/ObjectStatusList`

## Message Definition

```
std_msgs/Header header

int32 num_of_npcs
int32 num_of_pedestrian
int32 num_of_obstacle

ObjectStatus[] npc_list
ObjectStatus[] pedestrian_list
ObjectStatus[] obstacle_list


```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `num_of_npcs` | `int32` | - |
| `num_of_pedestrian` | `int32` | - |
| `num_of_obstacle` | `int32` | - |
| `npc_list` | `ObjectStatus[]` | - |
| `pedestrian_list` | `ObjectStatus[]` | - |
| `obstacle_list` | `ObjectStatus[]` | - |

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

