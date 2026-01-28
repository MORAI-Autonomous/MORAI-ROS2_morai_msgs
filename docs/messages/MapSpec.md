# MapSpec

**Message Type**: `morai_msgs/msg/MapSpec`

## Message Definition

```
std_msgs/Header header

int32 plane_coordinate_system
int32 utm_num

geometry_msgs/Vector3 utm_offset

string ellipse
float64 central_latitude
float64 central_meridian
float64 scale_factor
float64 false_easting
float64 false_northing```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `plane_coordinate_system` | `int32` | - |
| `utm_num` | `int32` | - |
| `utm_offset` | `geometry_msgs/Vector3` | - |
| `ellipse` | `string` | - |
| `central_latitude` | `float64` | - |
| `central_meridian` | `float64` | - |
| `scale_factor` | `float64` | - |
| `false_easting` | `float64` | - |
| `false_northing` | `float64` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import MapSpec

# Create message
msg = MapSpec()
msg.header = ''
msg.plane_coordinate_system = 0
msg.utm_num = 0
```

### C++

```cpp
#include <morai_msgs/msg/mapspec.hpp>

// Create message
auto msg = morai_msgs::msg::MapSpec();
msg.header = "";
msg.plane_coordinate_system = 0;
msg.utm_num = 0;
```

