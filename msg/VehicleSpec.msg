# VehicleSpec
# Vehicle specification data returned by the vehicle spec service.
# Service: /Service_MoraiVehicleSpec (response)

std_msgs/Header header

geometry_msgs/Vector3 size  # Vehicle dimensions (X, Y, Z) [m]
float32 wheel_base  # Distance between front and rear axles [m]
float64 max_steering  # Maximum steering angle [deg]

float32 overhang  # Front overhang length [m]
float32 rear_overhang  # Rear overhang length [m]
