# NpcGhostCmd

**Message Type**: `morai_msgs/msg/NpcGhostCmd`

## Message Definition

```
std_msgs/Header header

NpcGhostInfo[] npc_list
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `npc_list` | `NpcGhostInfo[]` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import NpcGhostCmd

# Create message
msg = NpcGhostCmd()
msg.header = ''
msg.npc_list = ''
```

### C++

```cpp
#include <morai_msgs/msg/npcghostcmd.hpp>

// Create message
auto msg = morai_msgs::msg::NpcGhostCmd();
msg.header = "";
msg.npc_list = "";
```

