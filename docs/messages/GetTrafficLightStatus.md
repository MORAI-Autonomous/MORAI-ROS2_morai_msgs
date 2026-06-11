# GetTrafficLightStatus

**Message Type**: `morai_msgs/msg/GetTrafficLightStatus`

Status of the closest traffic light to the ego vehicle.

**Topic**: `/GetTrafficLightStatus`

## Message Definition

```
# GetTrafficLightStatus
# Status of the closest traffic light to the ego vehicle.
# Topic: /GetTrafficLightStatus

std_msgs/Header header

string traffic_light_index  # Unique index of the traffic light
int16 traffic_light_type  # Light type (0: R/Y/G, 1: R/Y/G+left, 2: R/Y/G+left+G, 100: Y/Y/Y)
int16 traffic_light_status  # Current state (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `traffic_light_index` | `string` | Unique index of the traffic light |
| `traffic_light_type` | `int16` | Light type (0: R/Y/G, 1: R/Y/G+left, 2: R/Y/G+left+G, 100: Y/Y/Y) |
| `traffic_light_status` | `int16` | Current state (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit) |

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

