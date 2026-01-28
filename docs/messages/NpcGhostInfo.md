# NpcGhostInfo

**Message Type**: `morai_msgs/msg/NpcGhostInfo`

## Message Definition

```
int32 unique_id
string name

geometry_msgs/Vector3 position
geometry_msgs/Vector3 rpy
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `unique_id` | `int32` | - |
| `name` | `string` | - |
| `position` | `geometry_msgs/Vector3` | - |
| `rpy` | `geometry_msgs/Vector3` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import NpcGhostInfo

# Create message
msg = NpcGhostInfo()
msg.unique_id = 0
msg.name = ''
msg.position = ''
```

### C++

```cpp
#include <morai_msgs/msg/npcghostinfo.hpp>

// Create message
auto msg = morai_msgs::msg::NpcGhostInfo();
msg.unique_id = 0;
msg.name = "";
msg.position = "";
```

