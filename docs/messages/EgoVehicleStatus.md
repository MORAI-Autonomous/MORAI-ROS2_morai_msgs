# EgoVehicleStatus

**Message Type**: `morai_msgs/msg/EgoVehicleStatus`

## Message Definition

```
std_msgs/Header header
int32 unique_id
geometry_msgs/Vector3 acceleration
geometry_msgs/Vector3 position
geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 angular_velocity

float64 heading
float64 accel
float64 brake
float64 front_steer
float64 rear_steer

float32 tire_lateral_force_fl
float32 tire_lateral_force_fr
float32 tire_lateral_force_rl
float32 tire_lateral_force_rr

float32 side_slip_angle_fl
float32 side_slip_angle_fr
float32 side_slip_angle_rl
float32 side_slip_angle_rr

float32 tire_cornering_stiffness_fl
float32 tire_cornering_stiffness_fr
float32 tire_cornering_stiffness_rl
float32 tire_cornering_stiffness_rr

float32 distance_left_lane_boundary
float32 distance_right_lane_boundary
float32 cross_track_error```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `unique_id` | `int32` | - |
| `acceleration` | `geometry_msgs/Vector3` | - |
| `position` | `geometry_msgs/Vector3` | - |
| `velocity` | `geometry_msgs/Vector3` | - |
| `angular_velocity` | `geometry_msgs/Vector3` | - |
| `heading` | `float64` | - |
| `accel` | `float64` | - |
| `brake` | `float64` | - |
| `front_steer` | `float64` | - |
| `rear_steer` | `float64` | - |
| `tire_lateral_force_fl` | `float32` | - |
| `tire_lateral_force_fr` | `float32` | - |
| `tire_lateral_force_rl` | `float32` | - |
| `tire_lateral_force_rr` | `float32` | - |
| `side_slip_angle_fl` | `float32` | - |
| `side_slip_angle_fr` | `float32` | - |
| `side_slip_angle_rl` | `float32` | - |
| `side_slip_angle_rr` | `float32` | - |
| `tire_cornering_stiffness_fl` | `float32` | - |
| `tire_cornering_stiffness_fr` | `float32` | - |
| `tire_cornering_stiffness_rl` | `float32` | - |
| `tire_cornering_stiffness_rr` | `float32` | - |
| `distance_left_lane_boundary` | `float32` | - |
| `distance_right_lane_boundary` | `float32` | - |
| `cross_track_error` | `float32` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import EgoVehicleStatus

# Create message
msg = EgoVehicleStatus()
msg.header = ''
msg.unique_id = 0
msg.acceleration = ''
```

### C++

```cpp
#include <morai_msgs/msg/egovehiclestatus.hpp>

// Create message
auto msg = morai_msgs::msg::EgoVehicleStatus();
msg.header = "";
msg.unique_id = 0;
msg.acceleration = "";
```

