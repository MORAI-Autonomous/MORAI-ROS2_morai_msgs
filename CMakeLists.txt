cmake_minimum_required(VERSION 3.5)
project(morai_ros2_msgs)


find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/CollisionData.msg"
  "msg/CtrlCmd.msg"
  "msg/EgoVehicleStatus.msg"
  "msg/EventInfo.msg"
  "msg/GetTrafficLightStatus.msg"
  "msg/GPSMessage.msg"
  "msg/GhostCmd.msg"
  "msg/IntersectionControl.msg"
  "msg/IntersectionStatus.msg"
  "msg/Lamps.msg"
  "msg/MapSpec.msg"
  "msg/MoraiSimProcHandle.msg"
  "msg/MoraiSimProcStatus.msg"
  "msg/MoraiSrvResponse.msg"
  "msg/TrafficLightIndex.msg"
  "msg/TrafficLightInfo.msg"
  "msg/MultiEgoSetting.msg"
  "msg/NpcGhostCmd.msg"
  "msg/NpcGhostInfo.msg"
  "msg/ObjectStatus.msg"
  "msg/ObjectStatusList.msg"
  "msg/RadarDetection.msg"
  "msg/RadarDetections.msg"
  "msg/ReplayInfo.msg"
  "msg/SaveSensorData.msg"
  "msg/ScenarioLoad.msg"
  "msg/SensorPosControl.msg"
  "msg/SetTrafficLight.msg"
  "msg/VehicleCollision.msg"
  "msg/VehicleCollisionData.msg"
  "msg/VehicleSpec.msg"
  "msg/VehicleSpecIndex.msg"
)

set(srv_files
  "srv/EventCmd.srv"
  "srv/MapSpec.srv"
  "srv/ScenarioLoad.srv"
  "srv/MoraiSimProc.srv"
  "srv/TrafficLightInfo.srv"
  "srv/VehicleSpec.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files}
  DEPENDENCIES std_msgs geometry_msgs builtin_interfaces
)

ament_package()
