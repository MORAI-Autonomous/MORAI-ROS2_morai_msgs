# SensorPosControl

**Message Type**: `morai_msgs/msg/SensorPosControl`

Control sensor positions and orientations.

**Topic**: `/SensorPosControl`

## Message Definition

```
# SensorPosControl
# Control sensor positions and orientations.
# Topic: /SensorPosControl

int16[] sensor_index  # Sensor indices for identifying each sensor

float32[] pose_x  # Sensor X position [m]
float32[] pose_y  # Sensor Y position [m]
float32[] pose_z  # Sensor Z position [m]
float32[] roll   # Sensor roll angle [rad]
float32[] pitch  # Sensor pitch angle [rad]
float32[] yaw    # Sensor yaw angle [rad]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `sensor_index` | `int16[]` | Sensor indices for identifying each sensor |
| `pose_x` | `float32[]` | Sensor X position [m] |
| `pose_y` | `float32[]` | Sensor Y position [m] |
| `pose_z` | `float32[]` | Sensor Z position [m] |
| `roll` | `float32[]` | Sensor roll angle [rad] |
| `pitch` | `float32[]` | Sensor pitch angle [rad] |
| `yaw` | `float32[]` | Sensor yaw angle [rad] |

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

