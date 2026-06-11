# VehicleSpec

**Message Type**: `morai_msgs/msg/VehicleSpec`

Vehicle specification data returned by the vehicle spec service.

**Service**: `/Service_MoraiVehicleSpec (response)`

## Message Definition

```
# VehicleSpec
# Vehicle specification data returned by the vehicle spec service.
# Service: /Service_MoraiVehicleSpec (response)

std_msgs/Header header

geometry_msgs/Vector3 size  # Vehicle dimensions (X, Y, Z) [m]
float32 wheel_base  # Distance between front and rear axles [m]
float64 max_steering  # Maximum steering angle [deg]

float32 overhang  # Front overhang length [m]
float32 rear_overhang  # Rear overhang length [m]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `size` | `geometry_msgs/Vector3` | Vehicle dimensions (X, Y, Z) [m] |
| `wheel_base` | `float32` | Distance between front and rear axles [m] |
| `max_steering` | `float64` | Maximum steering angle [deg] |
| `overhang` | `float32` | Front overhang length [m] |
| `rear_overhang` | `float32` | Rear overhang length [m] |

## Usage Example

### Python

```python
from morai_msgs.msg import VehicleSpec

# Create message
msg = VehicleSpec()
msg.header = ''
msg.size = ''
msg.wheel_base = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/vehiclespec.hpp>

// Create message
auto msg = morai_msgs::msg::VehicleSpec();
msg.header = "";
msg.size = "";
msg.wheel_base = 0.0;
```

