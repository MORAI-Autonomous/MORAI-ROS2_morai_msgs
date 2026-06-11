# MoraiSimProc

**Service Type**: `morai_msgs/srv/MoraiSimProc`

Send rosbag replay playback commands to the simulator.

**Service**: `/Service_MoraiSimProc`

## Service Definition

```
# MoraiSimProc
# Send rosbag replay playback commands to the simulator.
# Service: /Service_MoraiSimProc

MoraiSimProcHandle request  # Playback command and conditions
---
MoraiSrvResponse response   # Success/failure result
```

## Request Fields

| Field | Type | Description |
|-------|------|-------------|
| `request` | `MoraiSimProcHandle` | Playback command and conditions |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `response` | `MoraiSrvResponse` | Success/failure result |

## Usage Example

### Python

```python
import rclpy
from rclpy.node import Node
from morai_msgs.srv import MoraiSimProc

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(MoraiSimProc, '/service_name')
        
    def call_service(self):
        request = MoraiSimProc.Request()
        # Set request fields
        future = self.client.call_async(request)
        return future
```

### C++

```cpp
#include <rclcpp/rclcpp.hpp>
#include <morai_msgs/srv/moraisimproc.hpp>

class ServiceClient : public rclcpp::Node {
public:
    ServiceClient() : Node("service_client") {
        client_ = this->create_client<morai_msgs::srv::MoraiSimProc>(
            "/service_name");
    }
    
    void call_service() {
        auto request = std::make_shared<morai_msgs::srv::MoraiSimProc::Request>();
        // Set request fields
        auto future = client_->async_send_request(request);
    }

private:
    rclcpp::Client<morai_msgs::srv::MoraiSimProc>::SharedPtr client_;
};
```

