# EventInfo

**Message Type**: `morai_msgs/msg/EventInfo`

One-time event control for vehicle state changes (used by the EventCmd service).

**Service**: `/Service_MoraiEventCmd (request/response)`

## Message Definition

```
# EventInfo
# One-time event control for vehicle state changes (used by the EventCmd service).
# Service: /Service_MoraiEventCmd (request/response)

std_msgs/Header header

int8 option  # Bitmask for fields to apply (1: ctrl_mode, 2: gear, 4: lamps, 8: set_pause)
int32 ctrl_mode  # Control mode (1: Keyboard, 2: Gamepad, 3: External, 6: Auto agent controlled)
int32 gear  # Gear selection (-1: No change, 1: Parking, 2: Reverse, 3: Neutral, 4: Drive)
Lamps lamps  # Vehicle lamp controls
bool set_pause  # true: pause simulation, false: continue
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `option` | `int8` | Bitmask for fields to apply (1: ctrl_mode, 2: gear, 4: lamps, 8: set_pause) |
| `ctrl_mode` | `int32` | Control mode (1: Keyboard, 2: Gamepad, 3: External, 6: Auto agent controlled) |
| `gear` | `int32` | Gear selection (-1: No change, 1: Parking, 2: Reverse, 3: Neutral, 4: Drive) |
| `lamps` | `Lamps` | Vehicle lamp controls |
| `set_pause` | `bool` | true: pause simulation, false: continue |

## Usage Example

### Python

```python
from morai_msgs.msg import EventInfo

# Create message
msg = EventInfo()
msg.header = ''
msg.option = 0
msg.ctrl_mode = 0
```

### C++

```cpp
#include <morai_msgs/msg/eventinfo.hpp>

// Create message
auto msg = morai_msgs::msg::EventInfo();
msg.header = "";
msg.option = 0;
msg.ctrl_mode = 0;
```

