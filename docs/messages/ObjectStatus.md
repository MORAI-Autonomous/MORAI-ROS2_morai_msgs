# ObjectStatus

**Message Type**: `morai_msgs/msg/ObjectStatus`

State information for a single object in the simulation.

## Message Definition

```
# ObjectStatus
# State information for a single object in the simulation.

int32 unique_id  # Object unique id
int32 type  # Object type (0: Pedestrian, 1: NPC vehicle, 2: Static object, -1: Ego vehicle)
string name  # Object name
float64 heading  # Object heading [deg]

geometry_msgs/Vector3 velocity  # Velocity vector [km/h]
geometry_msgs/Vector3 acceleration  # Acceleration vector [m/s^2]
geometry_msgs/Vector3 size  # Bounding box size (width, length, height) [m]
geometry_msgs/Vector3 position  # Position in ENU coordinates [m]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `unique_id` | `int32` | Object unique id |
| `type` | `int32` | Object type (0: Pedestrian, 1: NPC vehicle, 2: Static object, -1: Ego vehicle) |
| `name` | `string` | Object name |
| `heading` | `float64` | Object heading [deg] |
| `velocity` | `geometry_msgs/Vector3` | Velocity vector [km/h] |
| `acceleration` | `geometry_msgs/Vector3` | Acceleration vector [m/s^2] |
| `size` | `geometry_msgs/Vector3` | Bounding box size (width, length, height) [m] |
| `position` | `geometry_msgs/Vector3` | Position in ENU coordinates [m] |

## Usage Example

### Python

```python
from morai_msgs.msg import ObjectStatus

# Create message
msg = ObjectStatus()
msg.unique_id = 0
msg.type = 0
msg.name = ''
```

### C++

```cpp
#include <morai_msgs/msg/objectstatus.hpp>

// Create message
auto msg = morai_msgs::msg::ObjectStatus();
msg.unique_id = 0;
msg.type = 0;
msg.name = "";
```

