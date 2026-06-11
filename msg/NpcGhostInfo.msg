# NpcGhostInfo
# Information for a single NPC vehicle in ghost mode.

int32 unique_id  # NPC identifier
string name  # Model name (e.g., 2016_Kia_Niro(HEV))

geometry_msgs/Vector3 position  # Position in ENU coordinates [m]
geometry_msgs/Vector3 rpy  # Roll, Pitch, Yaw [deg]
