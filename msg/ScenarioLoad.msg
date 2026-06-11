# ScenarioLoad
# Load a scenario file and configure which data to include.
# Topic: /ScenarioLoad

std_msgs/Header header

string file_name  # Scenario file name to load
bool delete_all  # true: delete existing and load excluding ego vehicle, false: load all
bool load_network_connection_data  # true: load network connection data, false: skip
bool load_ego_vehicle_data  # true: load ego vehicle data, false: skip
bool load_surrounding_vehicle_data  # true: load NPC vehicle data, false: skip
bool load_pedestrian_data  # true: load pedestrian data, false: skip
bool load_obstacle_data  # true: load obstacle data, false: skip
bool set_pause  # true: pause after loading, false: play immediately
