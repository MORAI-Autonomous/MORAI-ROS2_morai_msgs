# GetTrafficLightStatus

**Message Type**: `morai_msgs/msg/GetTrafficLightStatus`

## Message Definition

```
std_msgs/Header header

string traffic_light_index
int16 traffic_light_type
int16 traffic_light_status
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `traffic_light_index` | `string` | - |
| `traffic_light_type` | `int16` | - |
| `traffic_light_status` | `int16` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import GetTrafficLightStatus

# Create message
msg = GetTrafficLightStatus()
msg.header = ''
msg.traffic_light_index = ''
msg.traffic_light_type = 0
```

### C++

```cpp
#include <morai_msgs/msg/gettrafficlightstatus.hpp>

// Create message
auto msg = morai_msgs::msg::GetTrafficLightStatus();
msg.header = "";
msg.traffic_light_index = "";
msg.traffic_light_type = 0;
```

