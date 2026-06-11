# SetTrafficLight

**Message Type**: `morai_msgs/msg/SetTrafficLight`

Control command to change a specific traffic light state.

**Topic**: `/SetTrafficLight`

## Message Definition

```
# SetTrafficLight
# Control command to change a specific traffic light state.
# Topic: /SetTrafficLight

std_msgs/Header header

string traffic_light_index  # Unique index of the traffic light
int16 traffic_light_status  # Target state (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `traffic_light_index` | `string` | Unique index of the traffic light |
| `traffic_light_status` | `int16` | Target state (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit) |

## Usage Example

### Python

```python
from morai_msgs.msg import SetTrafficLight

# Create message
msg = SetTrafficLight()
msg.header = ''
msg.traffic_light_index = ''
msg.traffic_light_status = 0
```

### C++

```cpp
#include <morai_msgs/msg/settrafficlight.hpp>

// Create message
auto msg = morai_msgs::msg::SetTrafficLight();
msg.header = "";
msg.traffic_light_index = "";
msg.traffic_light_status = 0;
```

