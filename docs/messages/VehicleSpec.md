# VehicleSpec

**Message Type**: `morai_msgs/msg/VehicleSpec`

## Message Definition

```
std_msgs/Header header

geometry_msgs/Vector3 size
float32 wheel_base
float64 max_steering

float32 overhang 
float32 rear_overhang
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `size` | `geometry_msgs/Vector3` | - |
| `wheel_base` | `float32` | - |
| `max_steering` | `float64` | - |
| `overhang` | `float32` | - |
| `rear_overhang` | `float32` | - |

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

