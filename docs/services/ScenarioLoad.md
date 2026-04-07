# ScenarioLoad

**Service Type**: `morai_msgs/srv/ScenarioLoad`

## Service Definition

```
ScenarioLoad request
---
MoraiSrvResponse response
```

## Request Fields

| Field | Type | Description |
|-------|------|-------------|
| `request` | `ScenarioLoad` | - |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `response` | `MoraiSrvResponse` | - |

## Usage Example

### Python

```python
import rclpy
from rclpy.node import Node
from morai_msgs.srv import ScenarioLoad

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(ScenarioLoad, '/service_name')
        
    def call_service(self):
        request = ScenarioLoad.Request()
        # Set request fields
        future = self.client.call_async(request)
        return future
```

### C++

```cpp
#include <rclcpp/rclcpp.hpp>
#include <morai_msgs/srv/scenarioload.hpp>

class ServiceClient : public rclcpp::Node {
public:
    ServiceClient() : Node("service_client") {
        client_ = this->create_client<morai_msgs::srv::ScenarioLoad>(
            "/service_name");
    }
    
    void call_service() {
        auto request = std::make_shared<morai_msgs::srv::ScenarioLoad::Request>();
        // Set request fields
        auto future = client_->async_send_request(request);
    }

private:
    rclcpp::Client<morai_msgs::srv::ScenarioLoad>::SharedPtr client_;
};
```

