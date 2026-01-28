# RadarDetection

**Message Type**: `morai_msgs/msg/RadarDetection`

## Message Definition

```
# This message relates only to FMCW radar.  
# All variables below are relative to the radar's frame of reference.
# This message is not meant to be used alone but as part of a stamped or array message.

# Object classifications (Additional vendor-specific classifications are permitted starting from 32000 eg. Car)

uint16 detection_id                       # Index of each radar detection point
geometry_msgs/Point position              # x, y, z position of each radar detection point

float32 azimuth							  # azimuth angle of each radar detection point in Degree
float32 rangerate						  # relative velocity of the radar detected target w.r.t radial direction
float32 amplitude						  # amplitude of the reflected signal of the radar detected target(rcs)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `detection_id` | `uint16` | Index of each radar detection point |
| `position` | `geometry_msgs/Point` | x, y, z position of each radar detection point |
| `azimuth` | `float32` | azimuth angle of each radar detection point in Degree |
| `rangerate` | `float32` | relative velocity of the radar detected target w.r.t radial direction |
| `amplitude` | `float32` | amplitude of the reflected signal of the radar detected target(rcs) |

## Usage Example

### Python

```python
from morai_msgs.msg import RadarDetection

# Create message
msg = RadarDetection()
msg.detection_id = 0
msg.position = 0
msg.azimuth = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/radardetection.hpp>

// Create message
auto msg = morai_msgs::msg::RadarDetection();
msg.detection_id = 0;
msg.position = 0;
msg.azimuth = 0.0;
```

