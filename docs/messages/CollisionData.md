# CollisionData

**Message Type**: `morai_msgs/msg/CollisionData`

Most recent collision between the ego vehicle and placed objects.

**Topic**: `/CollisionData`

## Message Definition

```
# CollisionData
# Most recent collision between the ego vehicle and placed objects.
# Topic: /CollisionData

std_msgs/Header header

float64 global_offset_x  # X-axis position w.r.t. map coordinate system
float64 global_offset_y  # Y-axis position w.r.t. map coordinate system
float64 global_offset_z  # Z-axis position w.r.t. map coordinate system

ObjectStatus[] collision_object  # Objects that collided with the ego vehicle
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `global_offset_x` | `float64` | X-axis position w.r.t. map coordinate system |
| `global_offset_y` | `float64` | Y-axis position w.r.t. map coordinate system |
| `global_offset_z` | `float64` | Z-axis position w.r.t. map coordinate system |
| `collision_object` | `ObjectStatus[]` | Objects that collided with the ego vehicle |

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

