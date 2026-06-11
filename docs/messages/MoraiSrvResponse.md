# MoraiSrvResponse

**Message Type**: `morai_msgs/msg/MoraiSrvResponse`

Generic service response indicating success or failure.

## Message Definition

```
# MoraiSrvResponse
# Generic service response indicating success or failure.

std_msgs/Header header

bool result  # true: success, false: failure
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `result` | `bool` | true: success, false: failure |

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

