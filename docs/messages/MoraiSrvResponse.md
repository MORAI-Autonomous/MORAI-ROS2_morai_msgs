# MoraiSrvResponse

**Message Type**: `morai_msgs/msg/MoraiSrvResponse`

## Message Definition

```
std_msgs/Header header

bool result```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `result` | `bool` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import MoraiSrvResponse

# Create message
msg = MoraiSrvResponse()
msg.header = ''
msg.result = ''
```

### C++

```cpp
#include <morai_msgs/msg/moraisrvresponse.hpp>

// Create message
auto msg = morai_msgs::msg::MoraiSrvResponse();
msg.header = "";
msg.result = "";
```

