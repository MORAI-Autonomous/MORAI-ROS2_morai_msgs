# TrafficLightInfo

**Message Type**: `morai_msgs/msg/TrafficLightInfo`

## Message Definition

```
std_msgs/Header header

string idx
int16 status
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `idx` | `string` | - |
| `status` | `int16` | - |

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

