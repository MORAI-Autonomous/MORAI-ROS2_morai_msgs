# SensorPosControl

**Message Type**: `morai_msgs/msg/SensorPosControl`

## Message Definition

```
int16[] sensor_index

float32[] pose_x
float32[] pose_y
float32[] pose_z
float32[] roll
float32[] pitch
float32[] yaw

```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `sensor_index` | `int16[]` | - |
| `pose_x` | `float32[]` | - |
| `pose_y` | `float32[]` | - |
| `pose_z` | `float32[]` | - |
| `roll` | `float32[]` | - |
| `pitch` | `float32[]` | - |
| `yaw` | `float32[]` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import SensorPosControl

# Create message
msg = SensorPosControl()
msg.sensor_index = 0
msg.pose_x = 0.0
msg.pose_y = 0.0
```

### C++

```cpp
#include <morai_msgs/msg/sensorposcontrol.hpp>

// Create message
auto msg = morai_msgs::msg::SensorPosControl();
msg.sensor_index = 0;
msg.pose_x = 0.0;
msg.pose_y = 0.0;
```

