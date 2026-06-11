# Lamps

**Message Type**: `morai_msgs/msg/Lamps`

Vehicle turn signal and emergency lamp control.

## Message Definition

```
# Lamps
# Vehicle turn signal and emergency lamp control.

std_msgs/Header header

int8 turn_signal  # Turn signal (0: No signal, 1: Left, 2: Right)
int8 emergency_signal  # Emergency signal (0: No signal, 1: Emergency lamps on)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `turn_signal` | `int8` | Turn signal (0: No signal, 1: Left, 2: Right) |
| `emergency_signal` | `int8` | Emergency signal (0: No signal, 1: Emergency lamps on) |

## Usage Example

### Python

```python
from morai_msgs.msg import Lamps

# Create message
msg = Lamps()
msg.header = ''
msg.turn_signal = 0
msg.emergency_signal = 0
```

### C++

```cpp
#include <morai_msgs/msg/lamps.hpp>

// Create message
auto msg = morai_msgs::msg::Lamps();
msg.header = "";
msg.turn_signal = 0;
msg.emergency_signal = 0;
```

