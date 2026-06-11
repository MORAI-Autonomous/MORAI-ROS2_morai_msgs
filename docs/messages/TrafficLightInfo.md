# TrafficLightInfo

**Message Type**: `morai_msgs/msg/TrafficLightInfo`

Traffic light information returned by the TrafficLightInfo service.

**Service**: `/Morai_TLSrv (response)`

## Message Definition

```
# TrafficLightInfo
# Traffic light information returned by the TrafficLightInfo service.
# Service: /Morai_TLSrv (response)

std_msgs/Header header

string idx  # Unique index of the traffic light
int16 status  # Light status (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `idx` | `string` | Unique index of the traffic light |
| `status` | `int16` | Light status (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit) |

## Usage Example

### Python

```python
from morai_msgs.msg import TrafficLightInfo

# Create message
msg = TrafficLightInfo()
msg.header = ''
msg.idx = ''
msg.status = 0
```

### C++

```cpp
#include <morai_msgs/msg/trafficlightinfo.hpp>

// Create message
auto msg = morai_msgs::msg::TrafficLightInfo();
msg.header = "";
msg.idx = "";
msg.status = 0;
```

