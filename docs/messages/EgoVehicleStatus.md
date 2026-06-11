# EgoVehicleStatus

**Message Type**: `morai_msgs/msg/EgoVehicleStatus`

Status telemetry of the ego vehicle for closed-loop control.

**Topic**: `/Ego_topic`

## Message Definition

```
# EgoVehicleStatus
# Status telemetry of the ego vehicle for closed-loop control.
# Topic: /Ego_topic

std_msgs/Header header
int32 unique_id  # Object unique id
geometry_msgs/Vector3 acceleration  # Acceleration vector [m/s^2]
geometry_msgs/Vector3 position  # Current position in ENU coordinates [m]
geometry_msgs/Vector3 velocity  # Velocity vector [m/s]
geometry_msgs/Vector3 angular_velocity  # Angular velocity [deg/s]

float64 heading  # Vehicle heading [deg]
float64 accel  # Accelerator pedal, range 0~1
float64 brake  # Brake pedal, range 0~1
float64 front_steer  # Front wheel angle [deg]
float64 rear_steer  # Rear wheel angle [deg]

float32 tire_lateral_force_fl  # Front-left tire lateral force
float32 tire_lateral_force_fr  # Front-right tire lateral force
float32 tire_lateral_force_rl  # Rear-left tire lateral force
float32 tire_lateral_force_rr  # Rear-right tire lateral force

float32 side_slip_angle_fl  # Front-left side slip angle
float32 side_slip_angle_fr  # Front-right side slip angle
float32 side_slip_angle_rl  # Rear-left side slip angle
float32 side_slip_angle_rr  # Rear-right side slip angle

float32 tire_cornering_stiffness_fl  # Front-left cornering stiffness
float32 tire_cornering_stiffness_fr  # Front-right cornering stiffness
float32 tire_cornering_stiffness_rl  # Rear-left cornering stiffness
float32 tire_cornering_stiffness_rr  # Rear-right cornering stiffness

float32 distance_left_lane_boundary  # Distance from left lane boundary [m]
float32 distance_right_lane_boundary  # Distance from right lane boundary [m]
float32 cross_track_error  # Distance from lane center, right-positive [m]
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `unique_id` | `int32` | Object unique id |
| `acceleration` | `geometry_msgs/Vector3` | Acceleration vector [m/s^2] |
| `position` | `geometry_msgs/Vector3` | Current position in ENU coordinates [m] |
| `velocity` | `geometry_msgs/Vector3` | Velocity vector [m/s] |
| `angular_velocity` | `geometry_msgs/Vector3` | Angular velocity [deg/s] |
| `heading` | `float64` | Vehicle heading [deg] |
| `accel` | `float64` | Accelerator pedal, range 0~1 |
| `brake` | `float64` | Brake pedal, range 0~1 |
| `front_steer` | `float64` | Front wheel angle [deg] |
| `rear_steer` | `float64` | Rear wheel angle [deg] |
| `tire_lateral_force_fl` | `float32` | Front-left tire lateral force |
| `tire_lateral_force_fr` | `float32` | Front-right tire lateral force |
| `tire_lateral_force_rl` | `float32` | Rear-left tire lateral force |
| `tire_lateral_force_rr` | `float32` | Rear-right tire lateral force |
| `side_slip_angle_fl` | `float32` | Front-left side slip angle |
| `side_slip_angle_fr` | `float32` | Front-right side slip angle |
| `side_slip_angle_rl` | `float32` | Rear-left side slip angle |
| `side_slip_angle_rr` | `float32` | Rear-right side slip angle |
| `tire_cornering_stiffness_fl` | `float32` | Front-left cornering stiffness |
| `tire_cornering_stiffness_fr` | `float32` | Front-right cornering stiffness |
| `tire_cornering_stiffness_rl` | `float32` | Rear-left cornering stiffness |
| `tire_cornering_stiffness_rr` | `float32` | Rear-right cornering stiffness |
| `distance_left_lane_boundary` | `float32` | Distance from left lane boundary [m] |
| `distance_right_lane_boundary` | `float32` | Distance from right lane boundary [m] |
| `cross_track_error` | `float32` | Distance from lane center, right-positive [m] |

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

