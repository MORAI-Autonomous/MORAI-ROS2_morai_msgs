# VehicleSpec

**Service Type**: `morai_msgs/srv/VehicleSpec`

Query the specification of a vehicle by unique id.

**Service**: `/Service_MoraiVehicleSpec`

## Service Definition

```
# VehicleSpec
# Query the specification of a vehicle by unique id.
# Service: /Service_MoraiVehicleSpec

VehicleSpecIndex request  # Unique id of the requested vehicle
---
VehicleSpec response      # Vehicle specification data
```

## Request Fields

| Field | Type | Description |
|-------|------|-------------|
| `request` | `VehicleSpecIndex` | Unique id of the requested vehicle |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `response` | `VehicleSpec` | Vehicle specification data |

## Usage Example

### Python

```python
import rclpy
from rclpy.node import Node
from morai_msgs.srv import VehicleSpec

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(VehicleSpec, '/service_name')
        
    def call_service(self):
        request = VehicleSpec.Request()
        # Set request fields
        future = self.client.call_async(request)
        return future
```

### C++

```cpp
#include <rclcpp/rclcpp.hpp>
#include <morai_msgs/srv/vehiclespec.hpp>

class ServiceClient : public rclcpp::Node {
public:
    ServiceClient() : Node("service_client") {
        client_ = this->create_client<morai_msgs::srv::VehicleSpec>(
            "/service_name");
    }
    
    void call_service() {
        auto request = std::make_shared<morai_msgs::srv::VehicleSpec::Request>();
        // Set request fields
        auto future = client_->async_send_request(request);
    }

private:
    rclcpp::Client<morai_msgs::srv::VehicleSpec>::SharedPtr client_;
};
```

