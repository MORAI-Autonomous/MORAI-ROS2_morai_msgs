# IntersectionStatus

**Message Type**: `morai_msgs/msg/IntersectionStatus`

## Message Definition

```
std_msgs/Header header
int32 intersection_index
int16 intersection_status
float32 intersection_status_time
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `intersection_index` | `int32` | - |
| `intersection_status` | `int16` | - |
| `intersection_status_time` | `float32` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import IntersectionStatus

# Create message
msg = IntersectionStatus()
msg.header = ''
msg.intersection_index = 0
msg.intersection_status = 0
```

### C++

```cpp
#include <morai_msgs/msg/intersectionstatus.hpp>

// Create message
auto msg = morai_msgs::msg::IntersectionStatus();
msg.header = "";
msg.intersection_index = 0;
msg.intersection_status = 0;
```

