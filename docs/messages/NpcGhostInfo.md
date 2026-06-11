# NpcGhostInfo

**Message Type**: `morai_msgs/msg/NpcGhostInfo`

Information for a single NPC vehicle in ghost mode.

## Message Definition

```
# NpcGhostInfo
# Information for a single NPC vehicle in ghost mode.

int32 unique_id  # NPC identifier
string name  # Model name (e.g., 2016_Kia_Niro(HEV))

geometry_msgs/Vector3 position  # Position in ENU coordinates [m]
geometry_msgs/Vector3 rpy  # Roll, Pitch, Yaw [deg]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `unique_id` | `int32` | NPC identifier |
| `name` | `string` | Model name (e.g., 2016_Kia_Niro(HEV)) |
| `position` | `geometry_msgs/Vector3` | Position in ENU coordinates [m] |
| `rpy` | `geometry_msgs/Vector3` | Roll, Pitch, Yaw [deg] |

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

