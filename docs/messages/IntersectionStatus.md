# IntersectionStatus

**Message Type**: `morai_msgs/msg/IntersectionStatus`

Current state of an intersection.

**Topic**: `/InsnStatus`

## Message Definition

```
# IntersectionStatus
# Current state of an intersection.
# Topic: /InsnStatus

std_msgs/Header header
int32 intersection_index  # Intersection identifier
int16 intersection_status  # Current intersection status
float32 intersection_status_time  # Elapsed time in current status [s]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `intersection_index` | `int32` | Intersection identifier |
| `intersection_status` | `int16` | Current intersection status |
| `intersection_status_time` | `float32` | Elapsed time in current status [s] |

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

