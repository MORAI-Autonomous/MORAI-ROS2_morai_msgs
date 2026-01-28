# CollisionData

**Message Type**: `morai_msgs/msg/CollisionData`

## Message Definition

```
std_msgs/Header header

float64 global_offset_x
float64 global_offset_y
float64 global_offset_z

ObjectStatus[] collision_object
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `global_offset_x` | `float64` | - |
| `global_offset_y` | `float64` | - |
| `global_offset_z` | `float64` | - |
| `collision_object` | `ObjectStatus[]` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import CollisionData

# Create message
msg = CollisionData()
msg.header = ''
msg.global_offset_x = 0.0
msg.global_offset_y = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/collisiondata.hpp>

// Create message
auto msg = morai_msgs::msg::CollisionData();
msg.header = "";
msg.global_offset_x = 0.0;
msg.global_offset_y = 0.0;
```

