#!/usr/bin/env python3
"""
Generate documentation pages for MORAI ROS2 messages and services.
"""

import os
from pathlib import Path

# Base paths
REPO_ROOT = Path(__file__).parent.parent
MSG_DIR = REPO_ROOT / "msg"
SRV_DIR = REPO_ROOT / "srv"
DOCS_MSG_DIR = REPO_ROOT / "docs" / "messages"
DOCS_SRV_DIR = REPO_ROOT / "docs" / "services"

# Ensure docs directories exist
DOCS_MSG_DIR.mkdir(parents=True, exist_ok=True)
DOCS_SRV_DIR.mkdir(parents=True, exist_ok=True)


def parse_msg_file(msg_path):
    """Parse a .msg file and return fields with comments."""
    fields = []
    current_comment = []
    
    with open(msg_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            
            # Skip empty lines
            if not line:
                current_comment = []
                continue
                
            # Handle comments
            if line.strip().startswith('#'):
                current_comment.append(line.strip()[1:].strip())
                continue
            
            # Parse field
            if line.strip():
                parts = line.split()
                if len(parts) >= 2:
                    field_type = parts[0]
                    field_name = parts[1]
                    
                    # Check for array notation
                    array_info = ""
                    if '[' in field_name:
                        field_name, array_part = field_name.split('[', 1)
                        array_info = f" [{array_part}"
                    
                    # Inline comment
                    inline_comment = ""
                    if '#' in line:
                        inline_comment = line.split('#', 1)[1].strip()
                    
                    comment = inline_comment if inline_comment else ' '.join(current_comment)
                    
                    fields.append({
                        'type': field_type,
                        'name': field_name,
                        'array': array_info,
                        'comment': comment
                    })
                    current_comment = []
    
    return fields


def parse_srv_file(srv_path):
    """Parse a .srv file and return request/response fields."""
    request_fields = []
    response_fields = []
    current_section = request_fields
    current_comment = []
    
    with open(srv_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            
            # Check for separator
            if line.strip() == '---':
                current_section = response_fields
                current_comment = []
                continue
            
            # Skip empty lines
            if not line:
                current_comment = []
                continue
                
            # Handle comments
            if line.strip().startswith('#'):
                current_comment.append(line.strip()[1:].strip())
                continue
            
            # Parse field
            if line.strip():
                parts = line.split()
                if len(parts) >= 2:
                    field_type = parts[0]
                    field_name = parts[1]
                    
                    # Check for array notation
                    array_info = ""
                    if '[' in field_name:
                        field_name, array_part = field_name.split('[', 1)
                        array_info = f" [{array_part}"
                    
                    # Inline comment
                    inline_comment = ""
                    if '#' in line:
                        inline_comment = line.split('#', 1)[1].strip()
                    
                    comment = inline_comment if inline_comment else ' '.join(current_comment)
                    
                    current_section.append({
                        'type': field_type,
                        'name': field_name,
                        'array': array_info,
                        'comment': comment
                    })
                    current_comment = []
    
    return request_fields, response_fields


def generate_msg_doc(msg_name, msg_path):
    """Generate markdown documentation for a message."""
    fields = parse_msg_file(msg_path)
    
    doc = f"# {msg_name}\n\n"
    doc += f"**Message Type**: `morai_msgs/msg/{msg_name}`\n\n"
    
    # Read raw content
    with open(msg_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
    
    doc += "## Message Definition\n\n"
    doc += "```\n"
    doc += raw_content
    doc += "```\n\n"
    
    if fields:
        doc += "## Field Descriptions\n\n"
        doc += "| Field | Type | Description |\n"
        doc += "|-------|------|-------------|\n"
        
        for field in fields:
            type_with_array = f"{field['type']}{field['array']}" if field['array'] else field['type']
            comment = field['comment'] if field['comment'] else "-"
            doc += f"| `{field['name']}` | `{type_with_array}` | {comment} |\n"
        doc += "\n"
    
    doc += "## Usage Example\n\n"
    doc += "### Python\n\n"
    doc += "```python\n"
    doc += f"from morai_msgs.msg import {msg_name}\n\n"
    doc += f"# Create message\n"
    doc += f"msg = {msg_name}()\n"
    if fields:
        for i, field in enumerate(fields[:3]):  # Show first 3 fields as example
            default_val = "0.0" if "float" in field['type'] else "0" if "int" in field['type'] else "''"
            doc += f"msg.{field['name']} = {default_val}\n"
    doc += "```\n\n"
    
    doc += "### C++\n\n"
    doc += "```cpp\n"
    doc += f"#include <morai_msgs/msg/{msg_name.lower()}.hpp>\n\n"
    doc += f"// Create message\n"
    doc += f"auto msg = morai_msgs::msg::{msg_name}();\n"
    if fields:
        for i, field in enumerate(fields[:3]):  # Show first 3 fields as example
            default_val = "0.0" if "float" in field['type'] else "0" if "int" in field['type'] else '""'
            doc += f"msg.{field['name']} = {default_val};\n"
    doc += "```\n\n"
    
    return doc


def generate_srv_doc(srv_name, srv_path):
    """Generate markdown documentation for a service."""
    request_fields, response_fields = parse_srv_file(srv_path)
    
    doc = f"# {srv_name}\n\n"
    doc += f"**Service Type**: `morai_msgs/srv/{srv_name}`\n\n"
    
    # Read raw content
    with open(srv_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
    
    doc += "## Service Definition\n\n"
    doc += "```\n"
    doc += raw_content
    doc += "```\n\n"
    
    if request_fields:
        doc += "## Request Fields\n\n"
        doc += "| Field | Type | Description |\n"
        doc += "|-------|------|-------------|\n"
        
        for field in request_fields:
            type_with_array = f"{field['type']}{field['array']}" if field['array'] else field['type']
            comment = field['comment'] if field['comment'] else "-"
            doc += f"| `{field['name']}` | `{type_with_array}` | {comment} |\n"
        doc += "\n"
    
    if response_fields:
        doc += "## Response Fields\n\n"
        doc += "| Field | Type | Description |\n"
        doc += "|-------|------|-------------|\n"
        
        for field in response_fields:
            type_with_array = f"{field['type']}{field['array']}" if field['array'] else field['type']
            comment = field['comment'] if field['comment'] else "-"
            doc += f"| `{field['name']}` | `{type_with_array}` | {comment} |\n"
        doc += "\n"
    
    doc += "## Usage Example\n\n"
    doc += "### Python\n\n"
    doc += "```python\n"
    doc += "import rclpy\n"
    doc += "from rclpy.node import Node\n"
    doc += f"from morai_msgs.srv import {srv_name}\n\n"
    doc += "class ServiceClient(Node):\n"
    doc += "    def __init__(self):\n"
    doc += "        super().__init__('service_client')\n"
    doc += f"        self.client = self.create_client({srv_name}, '/service_name')\n"
    doc += "        \n"
    doc += "    def call_service(self):\n"
    doc += f"        request = {srv_name}.Request()\n"
    doc += "        # Set request fields\n"
    doc += "        future = self.client.call_async(request)\n"
    doc += "        return future\n"
    doc += "```\n\n"
    
    doc += "### C++\n\n"
    doc += "```cpp\n"
    doc += "#include <rclcpp/rclcpp.hpp>\n"
    doc += f"#include <morai_msgs/srv/{srv_name.lower()}.hpp>\n\n"
    doc += "class ServiceClient : public rclcpp::Node {\n"
    doc += "public:\n"
    doc += "    ServiceClient() : Node(\"service_client\") {\n"
    doc += f"        client_ = this->create_client<morai_msgs::srv::{srv_name}>(\n"
    doc += "            \"/service_name\");\n"
    doc += "    }\n"
    doc += "    \n"
    doc += "    void call_service() {\n"
    doc += f"        auto request = std::make_shared<morai_msgs::srv::{srv_name}::Request>();\n"
    doc += "        // Set request fields\n"
    doc += "        auto future = client_->async_send_request(request);\n"
    doc += "    }\n\n"
    doc += "private:\n"
    doc += f"    rclcpp::Client<morai_msgs::srv::{srv_name}>::SharedPtr client_;\n"
    doc += "};\n"
    doc += "```\n\n"
    
    return doc


def main():
    """Generate all documentation pages."""
    print("Generating message documentation...")
    
    # Generate message docs
    msg_count = 0
    for msg_file in sorted(MSG_DIR.glob("*.msg")):
        msg_name = msg_file.stem
        doc_content = generate_msg_doc(msg_name, msg_file)
        
        doc_path = DOCS_MSG_DIR / f"{msg_name}.md"
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        print(f"  Created: {doc_path.relative_to(REPO_ROOT)}")
        msg_count += 1
    
    print(f"\nGenerated {msg_count} message documentation pages.")
    
    # Generate service docs
    print("\nGenerating service documentation...")
    srv_count = 0
    for srv_file in sorted(SRV_DIR.glob("*.srv")):
        srv_name = srv_file.stem
        doc_content = generate_srv_doc(srv_name, srv_file)
        
        doc_path = DOCS_SRV_DIR / f"{srv_name}.md"
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        print(f"  Created: {doc_path.relative_to(REPO_ROOT)}")
        srv_count += 1
    
    print(f"\nGenerated {srv_count} service documentation pages.")
    print(f"\nTotal: {msg_count + srv_count} documentation pages created!")
    print("\nTo view the documentation:")
    print("  1. Install dependencies: pip install mkdocs-material")
    print("  2. Run local server: mkdocs serve")
    print("  3. Open browser: http://127.0.0.1:8000")


if __name__ == "__main__":
    main()
