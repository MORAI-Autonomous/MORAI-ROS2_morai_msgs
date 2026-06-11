# MapSpec

**Message Type**: `morai_msgs/msg/MapSpec`

Map coordinate system specification (returned by the MapSpec service).

**Service**: `/Service_MoraiMapSpec (response)`

## Message Definition

```
# MapSpec
# Map coordinate system specification (returned by the MapSpec service).
# Service: /Service_MoraiMapSpec (response)

std_msgs/Header header

int32 plane_coordinate_system  # Coordinate system type (0: UTM CRS, 1: TM CRS)
int32 utm_num  # UTM zone number, range 1~60

geometry_msgs/Vector3 utm_offset  # Local offset [x, y, z]

string ellipse  # Ellipsoid type (e.g., WGS84, GRS80)
float64 central_latitude  # Central latitude (x-axis origin)
float64 central_meridian  # Central longitude (y-axis origin)
float64 scale_factor  # Scale multiplier, typically 1.0
float64 false_easting  # Additional x-axis offset
float64 false_northing  # Additional y-axis offset
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `plane_coordinate_system` | `int32` | Coordinate system type (0: UTM CRS, 1: TM CRS) |
| `utm_num` | `int32` | UTM zone number, range 1~60 |
| `utm_offset` | `geometry_msgs/Vector3` | Local offset [x, y, z] |
| `ellipse` | `string` | Ellipsoid type (e.g., WGS84, GRS80) |
| `central_latitude` | `float64` | Central latitude (x-axis origin) |
| `central_meridian` | `float64` | Central longitude (y-axis origin) |
| `scale_factor` | `float64` | Scale multiplier, typically 1.0 |
| `false_easting` | `float64` | Additional x-axis offset |
| `false_northing` | `float64` | Additional y-axis offset |

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

