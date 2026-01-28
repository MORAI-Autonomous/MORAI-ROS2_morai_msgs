# SetTrafficLight

**Message Type**: `morai_msgs/msg/SetTrafficLight`

## Message Definition

```
std_msgs/Header header

string traffic_light_index
int16 traffic_light_status
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `traffic_light_index` | `string` | - |
| `traffic_light_status` | `int16` | - |

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

