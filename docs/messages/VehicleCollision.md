# VehicleCollision

**Message Type**: `morai_msgs/msg/VehicleCollision`

A single collision event between NPC vehicles.

## Message Definition

```
# VehicleCollision
# A single collision event between NPC vehicles.

ObjectStatus[] crashed_vehicles  # List of collided NPC vehicles
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `crashed_vehicles` | `ObjectStatus[]` | List of collided NPC vehicles |

## Usage Example

### Python

```python
from morai_msgs.msg import VehicleCollision

# Create message
msg = VehicleCollision()
msg.crashed_vehicles = ''
```

### C++

```cpp
#include <morai_msgs/msg/vehiclecollision.hpp>

// Create message
auto msg = morai_msgs::msg::VehicleCollision();
msg.crashed_vehicles = "";
```

