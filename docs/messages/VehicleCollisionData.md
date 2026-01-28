# VehicleCollisionData

**Message Type**: `morai_msgs/msg/VehicleCollisionData`

## Message Definition

```
std_msgs/Header header
VehicleCollision[] collisions
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `collisions` | `VehicleCollision[]` | - |

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

