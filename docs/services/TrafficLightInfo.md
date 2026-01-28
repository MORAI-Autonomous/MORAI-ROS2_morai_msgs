# TrafficLightInfo

**Service Type**: `morai_msgs/srv/TrafficLightInfo`

## Service Definition

```
TrafficLightIndex request
---
TrafficLightInfo response```

## Request Fields

| Field | Type | Description |
|-------|------|-------------|
| `request` | `TrafficLightIndex` | - |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `response` | `TrafficLightInfo` | - |

## Usage Example

### Python

```python
import rclpy
from rclpy.node import Node
from morai_msgs.srv import TrafficLightInfo

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(TrafficLightInfo, '/service_name')
        
    def call_service(self):
        request = TrafficLightInfo.Request()
        # Set request fields
        future = self.client.call_async(request)
        return future
```

### C++

```cpp
#include <rclcpp/rclcpp.hpp>
#include <morai_msgs/srv/trafficlightinfo.hpp>

class ServiceClient : public rclcpp::Node {
public:
    ServiceClient() : Node("service_client") {
        client_ = this->create_client<morai_msgs::srv::TrafficLightInfo>(
            "/service_name");
    }
    
    void call_service() {
        auto request = std::make_shared<morai_msgs::srv::TrafficLightInfo::Request>();
        // Set request fields
        auto future = client_->async_send_request(request);
    }

private:
    rclcpp::Client<morai_msgs::srv::TrafficLightInfo>::SharedPtr client_;
};
```

