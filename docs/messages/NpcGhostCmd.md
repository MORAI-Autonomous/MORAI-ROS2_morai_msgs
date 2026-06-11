# NpcGhostCmd

**Message Type**: `morai_msgs/msg/NpcGhostCmd`

Control commands for NPC/traffic vehicles in ghost mode.

**Topic**: `/NpcGhost_Topic`

## Message Definition

```
# NpcGhostCmd
# Control commands for NPC/traffic vehicles in ghost mode.
# Topic: /NpcGhost_Topic

std_msgs/Header header

NpcGhostInfo[] npc_list  # Array of NPC ghost vehicle information
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `npc_list` | `NpcGhostInfo[]` | Array of NPC ghost vehicle information |

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

