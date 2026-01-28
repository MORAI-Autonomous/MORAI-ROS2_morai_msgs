# TrafficLightIndex

**Message Type**: `morai_msgs/msg/TrafficLightIndex`

## Message Definition

```
std_msgs/Header header

string idx
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `idx` | `string` | - |

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

