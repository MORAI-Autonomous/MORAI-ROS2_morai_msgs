# VehicleCollisionData
# Collisions between NPC vehicles (distinct from ego vehicle collisions).
# Topic: /VehicleCollisionData

std_msgs/Header header
VehicleCollision[] collisions  # List of NPC vehicle collision events
