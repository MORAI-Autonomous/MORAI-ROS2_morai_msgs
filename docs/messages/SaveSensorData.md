# SaveSensorData

**Message Type**: `morai_msgs/msg/SaveSensorData`

Configuration for saving sensor data to file.

**Topic**: `/SaveSensorData`

## Message Definition

```
# SaveSensorData
# Configuration for saving sensor data to file.
# Topic: /SaveSensorData

std_msgs/Header header

bool is_custom_file_name  # true: use custom filename, false: use default
string custom_file_name  # Custom filename input by user
string file_dir  # Full path of save directory
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `is_custom_file_name` | `bool` | true: use custom filename, false: use default |
| `custom_file_name` | `string` | Custom filename input by user |
| `file_dir` | `string` | Full path of save directory |

## Usage Example

### Python

```python
from morai_msgs.msg import SaveSensorData

# Create message
msg = SaveSensorData()
msg.header = ''
msg.is_custom_file_name = ''
msg.custom_file_name = ''
```

### C++

```cpp
#include <morai_msgs/msg/savesensordata.hpp>

// Create message
auto msg = morai_msgs::msg::SaveSensorData();
msg.header = "";
msg.is_custom_file_name = "";
msg.custom_file_name = "";
```

