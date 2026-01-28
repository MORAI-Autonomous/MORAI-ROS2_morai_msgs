# ObjectStatus

**Message Type**: `morai_msgs/msg/ObjectStatus`

## Message Definition

```
int32 unique_id
int32 type
string name
float64 heading

geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration
geometry_msgs/Vector3 size
geometry_msgs/Vector3 position
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `unique_id` | `int32` | - |
| `type` | `int32` | - |
| `name` | `string` | - |
| `heading` | `float64` | - |
| `velocity` | `geometry_msgs/Vector3` | - |
| `acceleration` | `geometry_msgs/Vector3` | - |
| `size` | `geometry_msgs/Vector3` | - |
| `position` | `geometry_msgs/Vector3` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import ObjectStatus

# Create message
msg = ObjectStatus()
msg.unique_id = 0
msg.type = 0
msg.name = ''
```

### C++

```cpp
#include <morai_msgs/msg/objectstatus.hpp>

// Create message
auto msg = morai_msgs::msg::ObjectStatus();
msg.unique_id = 0;
msg.type = 0;
msg.name = "";
```

