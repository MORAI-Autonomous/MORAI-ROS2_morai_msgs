# MultiEgoSetting

**Message Type**: `morai_msgs/msg/MultiEgoSetting`

Control multiple ego vehicles in the scene with external controllers.

**Topic**: `/ego_setting`

## Message Definition

```
# MultiEgoSetting
# Control multiple ego vehicles in the scene with external controllers.
# Topic: /ego_setting

std_msgs/Header header

int32 number_of_ego_vehicle  # Number of multi-ego vehicles
int32 camera_index  # Unique index of the viewed vehicle
int32[] ego_index  # Unique indices of multi-ego vehicles to control

float64[] global_position_x  # X-axis position of each multi-ego
float64[] global_position_y  # Y-axis position of each multi-ego
float64[] global_position_z  # Z-axis position (elevation) of each multi-ego
float32[] global_roll  # Roll angle of each multi-ego
float32[] global_pitch  # Pitch angle of each multi-ego
float32[] global_yaw  # Heading (yaw) angle of each multi-ego
float32[] velocity  # Velocity of each multi-ego
int8[] gear  # Gear of each multi-ego (1: Parking, 2: Reverse, 3: Neutral, 4: Drive)
int8[] ctrl_mode  # Control mode of each multi-ego (1: keyboard, 16: auto)
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `number_of_ego_vehicle` | `int32` | Number of multi-ego vehicles |
| `camera_index` | `int32` | Unique index of the viewed vehicle |
| `ego_index` | `int32[]` | Unique indices of multi-ego vehicles to control |
| `global_position_x` | `float64[]` | X-axis position of each multi-ego |
| `global_position_y` | `float64[]` | Y-axis position of each multi-ego |
| `global_position_z` | `float64[]` | Z-axis position (elevation) of each multi-ego |
| `global_roll` | `float32[]` | Roll angle of each multi-ego |
| `global_pitch` | `float32[]` | Pitch angle of each multi-ego |
| `global_yaw` | `float32[]` | Heading (yaw) angle of each multi-ego |
| `velocity` | `float32[]` | Velocity of each multi-ego |
| `gear` | `int8[]` | Gear of each multi-ego (1: Parking, 2: Reverse, 3: Neutral, 4: Drive) |
| `ctrl_mode` | `int8[]` | Control mode of each multi-ego (1: keyboard, 16: auto) |

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

