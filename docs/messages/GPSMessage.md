# GPSMessage

**Message Type**: `morai_msgs/msg/GPSMessage`

## Message Definition

```
std_msgs/Header header

float64 latitude
float64 longitude
float64 altitude

float64 east_offset
float64 north_offset
int16 status
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `latitude` | `float64` | - |
| `longitude` | `float64` | - |
| `altitude` | `float64` | - |
| `east_offset` | `float64` | - |
| `north_offset` | `float64` | - |
| `status` | `int16` | - |

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

