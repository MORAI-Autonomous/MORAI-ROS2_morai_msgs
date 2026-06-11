# VehicleCollisionData

**Message Type**: `morai_msgs/msg/VehicleCollisionData`

Collisions between NPC vehicles (distinct from ego vehicle collisions).

**Topic**: `/VehicleCollisionData`

## Message Definition

```
# VehicleCollisionData
# Collisions between NPC vehicles (distinct from ego vehicle collisions).
# Topic: /VehicleCollisionData

std_msgs/Header header
VehicleCollision[] collisions  # List of NPC vehicle collision events
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `collisions` | `VehicleCollision[]` | List of NPC vehicle collision events |

## Usage Example

### Python

```python
from morai_msgs.msg import VehicleCollisionData

# Create message
msg = VehicleCollisionData()
msg.header = ''
msg.collisions = ''
```

### C++

```cpp
#include <morai_msgs/msg/vehiclecollisiondata.hpp>

// Create message
auto msg = morai_msgs::msg::VehicleCollisionData();
msg.header = "";
msg.collisions = "";
```

