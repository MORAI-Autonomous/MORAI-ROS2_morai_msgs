# MORAI ROS2 Messages Documentation

Welcome to the documentation for the MORAI ROS2 message and service definitions package.

## Overview

The `morai_msgs` package provides ROS2 message and service definitions for interfacing with the MORAI autonomous driving simulator. This package enables communication between ROS2 nodes and the MORAI simulator for vehicle control, sensor data, and simulation management.

## Package Contents

### Messages

The package includes **32 message definitions** organized into the following categories:

- **Control Messages**: Vehicle control commands (CtrlCmd)
- **Vehicle Status**: Real-time vehicle state information (EgoVehicleStatus, VehicleSpec, Lamps)
- **Collision & Safety**: Collision detection and safety-related messages (CollisionData, VehicleCollision, VehicleCollisionData)
- **Traffic & Infrastructure**: Traffic lights, intersections, and infrastructure control (TrafficLightIndex, TrafficLightInfo, GetTrafficLightStatus, SetTrafficLight, IntersectionControl, IntersectionStatus)
- **Perception & Sensors**: Sensor data and object detection (ObjectStatus, ObjectStatusList, RadarDetection, RadarDetections, GPSMessage, SensorPosControl)
- **Simulation Control**: Simulator configuration and event management (MoraiSimProcHandle, MoraiSimProcStatus, MoraiSrvResponse, ScenarioLoad, EventInfo, ReplayInfo, SaveSensorData)
- **Ghost & NPC**: Non-player character control (GhostCmd, NpcGhostCmd, NpcGhostInfo)
- **Map**: Map specification and indexing (MapSpec, VehicleSpecIndex)
- **Multi-Vehicle**: Multi-ego vehicle settings (MultiEgoSetting)

### Services

The package includes **6 service definitions** for:

- Event management (EventCmd)
- Map specifications (MapSpec)
- Simulation process control (MoraiSimProc)
- Scenario loading (ScenarioLoad)
- Traffic light information (TrafficLightInfo)
- Vehicle specifications (VehicleSpec)

## Quick Start

### Installation

```bash
# Clone the repository
cd ~/ros2_ws/src
git clone https://github.com/MORAI-Autonomous/MORAI-ROS2_morai_msgs.git

# Build the package
cd ~/ros2_ws
colcon build --packages-select morai_msgs

# Source the workspace
source install/setup.bash
```

### Usage Example

```python
import rclpy
from rclpy.node import Node
from morai_msgs.msg import CtrlCmd

class VehicleController(Node):
    def __init__(self):
        super().__init__('vehicle_controller')
        self.publisher = self.create_publisher(CtrlCmd, '/ctrl_cmd', 10)
        
    def send_control_command(self, accel, brake, steering):
        msg = CtrlCmd()
        msg.longl_cmd_type = 2  # Acceleration command
        msg.accel = accel
        msg.brake = brake
        msg.steering = steering
        self.publisher.publish(msg)
```

## Navigation

Use the navigation menu on the left to explore:

- **[Messages](messages/index.md)**: Browse all message definitions by category
- **[Services](services/index.md)**: Browse all service definitions

## Resources

- [GitHub Repository](https://github.com/MORAI-Autonomous/MORAI-ROS2_morai_msgs)
- [MORAI Official Website](https://www.morai.ai/)

## License

See the [LICENSE](https://github.com/MORAI-Autonomous/MORAI-ROS2_morai_msgs/blob/main/LICENSE) file for details.
