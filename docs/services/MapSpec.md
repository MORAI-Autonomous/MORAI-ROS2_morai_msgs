# MapSpec

**Service Type**: `morai_msgs/srv/MapSpec`

## Service Definition

```
std_msgs/Empty empty
---
MapSpec response```

## Request Fields

| Field | Type | Description |
|-------|------|-------------|
| `empty` | `std_msgs/Empty` | - |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `response` | `MapSpec` | - |

## Usage Example

### Python

```python
import rclpy
from rclpy.node import Node
from morai_msgs.srv import MapSpec

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(MapSpec, '/service_name')
        
    def call_service(self):
        request = MapSpec.Request()
        # Set request fields
        future = self.client.call_async(request)
        return future
```

### C++

```cpp
#include <rclcpp/rclcpp.hpp>
#include <morai_msgs/srv/mapspec.hpp>

class ServiceClient : public rclcpp::Node {
public:
    ServiceClient() : Node("service_client") {
        client_ = this->create_client<morai_msgs::srv::MapSpec>(
            "/service_name");
    }
    
    void call_service() {
        auto request = std::make_shared<morai_msgs::srv::MapSpec::Request>();
        // Set request fields
        auto future = client_->async_send_request(request);
    }

private:
    rclcpp::Client<morai_msgs::srv::MapSpec>::SharedPtr client_;
};
```

