# ScenarioLoad

**Message Type**: `morai_msgs/msg/ScenarioLoad`

## Message Definition

```
std_msgs/Header header

string file_name
bool delete_all
bool load_network_connection_data
bool load_ego_vehicle_data
bool load_surrounding_vehicle_data
bool load_pedestrian_data
bool load_obstacle_data
bool set_pause
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `file_name` | `string` | - |
| `delete_all` | `bool` | - |
| `load_network_connection_data` | `bool` | - |
| `load_ego_vehicle_data` | `bool` | - |
| `load_surrounding_vehicle_data` | `bool` | - |
| `load_pedestrian_data` | `bool` | - |
| `load_obstacle_data` | `bool` | - |
| `set_pause` | `bool` | - |

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

