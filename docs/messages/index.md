# Messages Overview

This section contains documentation for all 32 ROS2 message definitions in the `morai_msgs` package.

## Message Categories

### Control Messages
Messages for controlling vehicle motion and behavior:

- **[CtrlCmd](CtrlCmd.md)** - Basic vehicle control command

### Vehicle Status
Messages containing real-time vehicle state information:

- **[EgoVehicleStatus](EgoVehicleStatus.md)** - Complete ego vehicle status
- **[VehicleSpec](VehicleSpec.md)** - Vehicle specifications
- **[VehicleSpecIndex](VehicleSpecIndex.md)** - Vehicle specification index
- **[Lamps](Lamps.md)** - Vehicle lamp status

### Collision & Safety
Messages related to collision detection and safety:

- **[CollisionData](CollisionData.md)** - Collision event data
- **[VehicleCollision](VehicleCollision.md)** - Vehicle collision information
- **[VehicleCollisionData](VehicleCollisionData.md)** - Detailed collision data

### Traffic & Infrastructure
Messages for traffic lights and infrastructure control:

- **[GetTrafficLightStatus](GetTrafficLightStatus.md)** - Query traffic light status
- **[SetTrafficLight](SetTrafficLight.md)** - Set traffic light state
- **[TrafficLightIndex](TrafficLightIndex.md)** - Traffic light index
- **[TrafficLightInfo](TrafficLightInfo.md)** - Traffic light information
- **[IntersectionControl](IntersectionControl.md)** - Intersection control command
- **[IntersectionStatus](IntersectionStatus.md)** - Intersection status

### Perception & Sensors
Messages for sensor data and object detection:

- **[ObjectStatus](ObjectStatus.md)** - Single object status
- **[ObjectStatusList](ObjectStatusList.md)** - Multiple object statuses
- **[RadarDetection](RadarDetection.md)** - Single radar detection
- **[RadarDetections](RadarDetections.md)** - Multiple radar detections
- **[GPSMessage](GPSMessage.md)** - GPS data
- **[SensorPosControl](SensorPosControl.md)** - Sensor position control

### Simulation Control
Messages for simulator configuration and management:

- **[MoraiSimProcHandle](MoraiSimProcHandle.md)** - Simulator process handle
- **[MoraiSimProcStatus](MoraiSimProcStatus.md)** - Simulator process status
- **[MoraiSrvResponse](MoraiSrvResponse.md)** - Service response message
- **[ScenarioLoad](ScenarioLoad.md)** - Scenario loading
- **[EventInfo](EventInfo.md)** - Event information
- **[ReplayInfo](ReplayInfo.md)** - Replay information
- **[SaveSensorData](SaveSensorData.md)** - Save sensor data command

### Ghost & NPC
Messages for non-player character control:

- **[GhostCmd](GhostCmd.md)** - Ghost vehicle command
- **[NpcGhostCmd](NpcGhostCmd.md)** - NPC ghost command
- **[NpcGhostInfo](NpcGhostInfo.md)** - NPC ghost information

### Map
Messages for map specifications:

- **[MapSpec](MapSpec.md)** - Map specification

### Multi-Vehicle
Messages for multi-vehicle scenarios:

- **[MultiEgoSetting](MultiEgoSetting.md)** - Multi-ego vehicle settings

## Usage

To use any message in your ROS2 node:

```python
from morai_msgs.msg import CtrlCmd

# Create a message instance
msg = CtrlCmd()
msg.accel = 0.5
msg.brake = 0.0
msg.steering = 0.1
```

Or in C++:

```cpp
#include <morai_msgs/msg/ctrl_cmd.hpp>

auto msg = morai_msgs::msg::CtrlCmd();
msg.accel = 0.5;
msg.brake = 0.0;
msg.steering = 0.1;
```
