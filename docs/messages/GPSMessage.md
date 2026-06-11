# GPSMessage

**Message Type**: `morai_msgs/msg/GPSMessage`

GPS position data with local coordinate offsets.

**Topic**: `/gps`

## Message Definition

```
# GPSMessage
# GPS position data with local coordinate offsets.
# Topic: /gps

std_msgs/Header header

float64 latitude  # Geographic latitude [deg]
float64 longitude  # Geographic longitude [deg]
float64 altitude  # Altitude above sea level [m]

float64 east_offset  # East (X) offset from map origin [m]
float64 north_offset  # North (Y) offset from map origin [m]
int16 status  # GPS status indicator
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `latitude` | `float64` | Geographic latitude [deg] |
| `longitude` | `float64` | Geographic longitude [deg] |
| `altitude` | `float64` | Altitude above sea level [m] |
| `east_offset` | `float64` | East (X) offset from map origin [m] |
| `north_offset` | `float64` | North (Y) offset from map origin [m] |
| `status` | `int16` | GPS status indicator |

## Usage Example

### Python

```python
from morai_msgs.msg import GPSMessage

# Create message
msg = GPSMessage()
msg.header = ''
msg.latitude = 0.0
msg.longitude = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/gpsmessage.hpp>

// Create message
auto msg = morai_msgs::msg::GPSMessage();
msg.header = "";
msg.latitude = 0.0;
msg.longitude = 0.0;
```

