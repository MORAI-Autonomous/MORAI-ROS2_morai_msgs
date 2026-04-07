# RadarDetections

**Message Type**: `morai_msgs/msg/RadarDetections`

## Message Definition

```
std_msgs/Header header

RadarDetection[] detections
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `header` | `std_msgs/Header` | - |
| `detections` | `RadarDetection[]` | - |

## Usage Example

### Python

```python
from morai_msgs.msg import RadarDetections

# Create message
msg = RadarDetections()
msg.header = ''
msg.detections = ''
```

### C++

```cpp
#include <morai_msgs/msg/radardetections.hpp>

// Create message
auto msg = morai_msgs::msg::RadarDetections();
msg.header = "";
msg.detections = "";
```

