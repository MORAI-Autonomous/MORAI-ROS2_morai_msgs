# ScenarioLoad

**Message Type**: `morai_msgs/msg/ScenarioLoad`

Load a scenario file and configure which data to include.

**Topic**: `/ScenarioLoad`

## Message Definition

```
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
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `file_name` | `string` | Scenario file name to load |
| `delete_all` | `bool` | true: delete existing and load excluding ego vehicle, false: load all |
| `load_network_connection_data` | `bool` | true: load network connection data, false: skip |
| `load_ego_vehicle_data` | `bool` | true: load ego vehicle data, false: skip |
| `load_surrounding_vehicle_data` | `bool` | true: load NPC vehicle data, false: skip |
| `load_pedestrian_data` | `bool` | true: load pedestrian data, false: skip |
| `load_obstacle_data` | `bool` | true: load obstacle data, false: skip |
| `set_pause` | `bool` | true: pause after loading, false: play immediately |

## Usage Example

### Python

```python
from morai_msgs.msg import ScenarioLoad

# Create message
msg = ScenarioLoad()
msg.header = ''
msg.file_name = ''
msg.delete_all = ''
```

### C++

```cpp
#include <morai_msgs/msg/scenarioload.hpp>

// Create message
auto msg = morai_msgs::msg::ScenarioLoad();
msg.header = "";
msg.file_name = "";
msg.delete_all = "";
```

