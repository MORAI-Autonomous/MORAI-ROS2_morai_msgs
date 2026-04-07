# Lamps

**Message Type**: `morai_msgs/msg/Lamps`

## Message Definition

```
std_msgs/Header header

int8 turn_signal
int8 emergency_signal
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `turn_signal` | `int8` | - |
| `emergency_signal` | `int8` | - |

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

