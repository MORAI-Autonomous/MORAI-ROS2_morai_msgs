# MultiEgoSetting

**Message Type**: `morai_msgs/msg/MultiEgoSetting`

## Message Definition

```
std_msgs/Header header

int32 number_of_ego_vehicle
int32 camera_index
int32[] ego_index

float64[] global_position_x
float64[] global_position_y
float64[] global_position_z
float32[] global_roll
float32[] global_pitch
float32[] global_yaw
float32[] velocity
int8[] gear
int8[] ctrl_mode
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `number_of_ego_vehicle` | `int32` | - |
| `camera_index` | `int32` | - |
| `ego_index` | `int32[]` | - |
| `global_position_x` | `float64[]` | - |
| `global_position_y` | `float64[]` | - |
| `global_position_z` | `float64[]` | - |
| `global_roll` | `float32[]` | - |
| `global_pitch` | `float32[]` | - |
| `global_yaw` | `float32[]` | - |
| `velocity` | `float32[]` | - |
| `gear` | `int8[]` | - |
| `ctrl_mode` | `int8[]` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import MultiEgoSetting

# Create message
msg = MultiEgoSetting()
msg.header = ''
msg.number_of_ego_vehicle = 0
msg.camera_index = 0
```

### C++

```cpp
#include <morai_msgs/msg/multiegosetting.hpp>

// Create message
auto msg = morai_msgs::msg::MultiEgoSetting();
msg.header = "";
msg.number_of_ego_vehicle = 0;
msg.camera_index = 0;
```

