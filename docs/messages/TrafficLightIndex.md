# TrafficLightIndex

**Message Type**: `morai_msgs/msg/TrafficLightIndex`

Traffic light query request for the TrafficLightInfo service.

**Service**: `/Morai_TLSrv (request)`

## Message Definition

```
# TrafficLightIndex
# Traffic light query request for the TrafficLightInfo service.
# Service: /Morai_TLSrv (request)

std_msgs/Header header

string idx  # Unique ID of the requested traffic light
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `idx` | `string` | Unique ID of the requested traffic light |

## Usage Example

### Python

```python
from morai_msgs.msg import TrafficLightIndex

# Create message
msg = TrafficLightIndex()
msg.header = ''
msg.idx = ''
```

### C++

```cpp
#include <morai_msgs/msg/trafficlightindex.hpp>

// Create message
auto msg = morai_msgs::msg::TrafficLightIndex();
msg.header = "";
msg.idx = "";
```

