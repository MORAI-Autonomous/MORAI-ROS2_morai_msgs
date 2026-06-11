# VehicleSpecIndex

**Message Type**: `morai_msgs/msg/VehicleSpecIndex`

Vehicle specification query request.

**Service**: `/Service_MoraiVehicleSpec (request)`

## Message Definition

```
# VehicleSpecIndex
# Vehicle specification query request.
# Service: /Service_MoraiVehicleSpec (request)

std_msgs/Header header

int32 unique_id  # Unique ID of the requested vehicle
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `unique_id` | `int32` | Unique ID of the requested vehicle |

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

