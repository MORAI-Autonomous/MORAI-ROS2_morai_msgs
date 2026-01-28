# VehicleSpecIndex

**Message Type**: `morai_msgs/msg/VehicleSpecIndex`

## Message Definition

```
std_msgs/Header header

int32 unique_id```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `unique_id` | `int32` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import VehicleSpecIndex

# Create message
msg = VehicleSpecIndex()
msg.header = ''
msg.unique_id = 0
```

### C++

```cpp
#include <morai_msgs/msg/vehiclespecindex.hpp>

// Create message
auto msg = morai_msgs::msg::VehicleSpecIndex();
msg.header = "";
msg.unique_id = 0;
```

