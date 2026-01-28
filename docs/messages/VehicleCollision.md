# VehicleCollision

**Message Type**: `morai_msgs/msg/VehicleCollision`

## Message Definition

```
ObjectStatus[] crashed_vehicles
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `crashed_vehicles` | `ObjectStatus[]` | - |

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

