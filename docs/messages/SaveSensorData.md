# SaveSensorData

**Message Type**: `morai_msgs/msg/SaveSensorData`

## Message Definition

```
std_msgs/Header header

bool is_custom_file_name
string custom_file_name
string file_dir
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `is_custom_file_name` | `bool` | - |
| `custom_file_name` | `string` | - |
| `file_dir` | `string` | - |

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

