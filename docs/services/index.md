# Services Overview

This section contains documentation for all 6 ROS2 service definitions in the `morai_msgs` package.

## Available Services

### Event Management

- **[EventCmd](EventCmd.md)** - Send event commands to simulator

### Map & Environment

- **[MapSpec](MapSpec.md)** - Query map specifications
- **[TrafficLightInfo](TrafficLightInfo.md)** - Query traffic light information

### Simulation Management

- **[MoraiSimProc](MoraiSimProc.md)** - Control simulator process lifecycle
- **[ScenarioLoad](ScenarioLoad.md)** - Load simulation scenarios

### Vehicle Configuration

- **[VehicleSpec](VehicleSpec.md)** - Query vehicle specifications

## Service Usage

### Python Example

```python
import rclpy
from rclpy.node import Node
from morai_msgs.srv import MoraiSimProc

class SimControlNode(Node):
    def __init__(self):
        super().__init__('sim_control_node')
        self.client = self.create_client(MoraiSimProc, '/morai_sim_proc')
        
    def call_service(self):
        request = MoraiSimProc.Request()
        # Set request fields
        future = self.client.call_async(request)
        return future

# Usage
node = SimControlNode()
future = node.call_service()
rclpy.spin_until_future_complete(node, future)
response = future.result()
```

### C++ Example

```cpp
#include <rclcpp/rclcpp.hpp>
#include <morai_msgs/srv/morai_sim_proc.hpp>

class SimControlNode : public rclcpp::Node {
public:
    SimControlNode() : Node("sim_control_node") {
        client_ = this->create_client<morai_msgs::srv::MoraiSimProc>(
            "/morai_sim_proc");
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

## Service Structure

ROS2 services follow a request-response pattern:

```
Request Fields
---
Response Fields
```

Each service documentation page provides:

- Service definition
- Field descriptions
- Usage examples
- Related messages
