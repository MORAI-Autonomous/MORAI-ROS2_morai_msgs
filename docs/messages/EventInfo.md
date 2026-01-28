# EventInfo

**Message Type**: `morai_msgs/msg/EventInfo`

## Message Definition

```
std_msgs/Header header

int8 option
int32 ctrl_mode
int32 gear
Lamps lamps
bool set_pause
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `option` | `int8` | - |
| `ctrl_mode` | `int32` | - |
| `gear` | `int32` | - |
| `lamps` | `Lamps` | - |
| `set_pause` | `bool` | - |

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

