cmake_minimum_required(VERSION 3.5)
project(morai_msgs)


find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/CollisionData.msg"
  "msg/CtrlCmd.msg"
  "msg/EgoVehiclePosition.msg"
  "msg/EgoVehicleStatus.msg"
  "msg/EgoVehicleVelocity.msg"
  "msg/FactoryAddress.msg"
  "msg/GPSMessage.msg"
  "msg/GuideData.msg"
  "msg/ObjectInfo.msg"
  "msg/ScenarioLoad.msg"
  "msg/SVehicleStatus.msg"
  "msg/TrafficLight.msg"
  "msg/VehicleCommand.msg"
  "msg/VelPlot.msg"
  "msg/ERP42Info.msg"
  "msg/GetTrafficLightStatus.msg"
  "msg/SetTrafficLight.msg"
  "msg/IntersectionControl.msg"
  "msg/IntersectionStatus.msg"
  "msg/MultiEgoSetting.msg"
  "msg/IntscnTL.msg"
  "msg/SensorPosControl.msg"
  "msg/GenericVehicleControl.msg"
  "msg/SaveSensorData.msg"
  "msg/MoraiTimestamp.msg"
  "msg/GhostMessage.msg"
  "msg/Lamps.msg"
  "msg/MoraiTLInfo.msg"
  "msg/MoraiSimProcHandle.msg"
  "msg/MoraiSimProcStatus.msg"
  "msg/MoraiSrvResponse.msg"
  "msg/MoraiTLIndex.msg"
  "msg/RadarTrack.msg"
  "msg/RadarTracks.msg"
  "msg/Mgeo.msg"
  "msg/MgeoLink.msg"
  "msg/MgeoLinkList.msg"
  "msg/MgeoNode.msg"
  "msg/MgeoNodeList.msg"
  "msg/EventInfo.msg"
  "msg/ReplayInfo.msg"
  "msg/ObjectStatus.msg"
  "msg/ObjectStatusList.msg"
  "msg/VehicleSpecIndex.msg"
  "msg/VehicleSpec.msg"
  "msg/VehicleCollision.msg"
  "msg/VehicleCollisionData.msg"
  "msg/NpcGhostCmd.msg"
  "msg/NpcGhostInfo.msg"
)

set(srv_files
  "srv/MoraiScenarioLoadSrv.srv"
  "srv/MoraiSimProcSrv.srv"
  "srv/MoraiTLInfoSrv.srv"
  "srv/MoraiVehicleSpecSrv.srv"
  "srv/MoraiEventCmdSrv.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files}
  DEPENDENCIES std_msgs geometry_msgs builtin_interfaces
)

ament_package()