# FastMCP Server

This repo helps you to build your simple MCP server on an EC2 instance and then connect it to Cursor or similar AI clients. This repository contains a lightweight MCP (Model Context Protocol) server built with FastMCP that provides utility tools and resources to AI assistants, including weather information, unit conversions, and sample data resources.

## What is MCP?

**MCP (Model Context Protocol)** is an open protocol that enables AI assistants to connect to external data sources and tools. It allows AI models to:

- Access real-time information from external APIs
- Execute tools and functions
- Retrieve resources and data
- Interact with databases, file systems, and other services

Think of MCP as a "bridge" that connects AI assistants to the external world, enabling them to go beyond their training data and access current, dynamic information.

## MCP vs Traditional APIs

| Aspect | MCP | Traditional APIs |
|--------|-----|------------------|
| **Purpose** | AI assistant integration | Application-to-application communication |
| **Protocol** | Standardized protocol for AI tools | Various protocols (REST, GraphQL, gRPC) |
| **Authentication** | Built-in security model | Custom authentication schemes |
| **Tool Discovery** | Automatic tool registration and discovery | Manual API documentation and integration |
| **AI-Optimized** | Designed for AI assistant workflows | Designed for programmatic access |
| **Real-time** | Supports streaming and real-time updates | Typically request-response based |

## What is FastMCP?

**FastMCP** is a Python framework that simplifies building MCP servers. It provides:

- **Decorator-based tool definitions** - Easy function-to-tool conversion
- **Built-in transport layers** - HTTP, WebSocket, and streaming support
- **Automatic schema generation** - Type hints become tool schemas
- **Resource management** - Serve static and dynamic resources
- **Prompt templates** - Guide AI assistants on tool usage

### Transport Configuration

This server uses `transport="streamable-http"` which provides:
- **Real-time streaming** - Supports live data updates and long-running operations
- **HTTP compatibility** - Works with standard HTTP clients and load balancers
- **Efficient communication** - Reduces latency for AI assistant interactions

## FastMCP Components

### 1. Tools (`@app.tool()`)

Tools are functions that AI assistants can call to perform actions or retrieve information.

```python
@app.tool()
def get_weather(city: str):
    """Fetch current weather for a city."""
    return {"city": city, "weather": f"Sample weather for {city}: sunny 25°C"}
```

**Features:**
- Automatic parameter validation
- Type hint conversion to JSON schema
- Docstring becomes tool description
- Return values automatically serialized

### 2. Resources (`@app.resource()`)

Resources provide static or dynamic data that AI assistants can access.

```python
@app.resource("resource://sample-weather")
def sample_weather():
    """Static resource with example weather data."""
    return {"city": "London", "weather": "London: partly cloudy, +18°C"}
```

**Features:**
- URI-based access (`resource://sample-weather`)
- Can be static data or computed dynamically
- Supports various data formats

### 3. Prompts (`@app.prompt()`)

Prompts guide AI assistants on how to use the available tools.

```python
@app.prompt()
def weather_prompt():
    return "Ask me about the weather like: get_weather(city='Paris')"
```

**Features:**
- Provide usage examples
- Guide AI behavior
- Improve tool discovery

## Deployment on EC2 with uv

### Prerequisites

- EC2 instance with Ubuntu/Debian
- Add security group rule for inbound traffic on port 8000
- Python 3.8+ installed
- `uv` package manager

### Step 1: Install uv

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload shell
source ~/.bashrc
```

### Step 2: Clone and Setup Project

```bash
# Clone your repository
git clone <your-repo-url>
cd fastmcp

# Create virtual environment with Python 3.11
uv venv --python 3.11
source .venv/bin/activate

# Initialize uv project and add dependencies
uv init
uv add fastmcp requests

# Run the server
uv run mcp-server.py
```
<img width="1138" height="553" alt="image" src="https://github.com/user-attachments/assets/1ea11066-d5d8-4016-97f0-5b0e63211698" />


### Step 3: Configure Firewall

```bash
# Allow port 8000 (adjust as needed)
sudo ufw allow 8000
```

## Connecting to IDEs

### Cursor IDE

Create or edit your `mcp.json` configuration file:

```json
{
  "mcpServers": {
    "utility-mcp-server": {
      "autoApprove": [],
      "disabled": false,
      "transportType": "streamable-http",
      "url": "http://<Public-IP-EC2>:8000/mcp"
    }
  }
}
```

### Other IDEs

Most IDEs support MCP through similar configuration patterns. Check your IDE's MCP documentation for specific syntax.

## Testing the Connection

1. **Restart your IDE** after adding MCP configuration
2. **Check MCP status** in your IDE's MCP panel
3. **Test tools** by asking your AI assistant to use them:

```
"Get the weather for Tokyo"
"Convert 50 miles to kilometers"
"Show me the sample weather resource"
```
<img width="620" height="434" alt="image" src="https://github.com/user-attachments/assets/477a2ac5-fc50-4b59-a11c-dec6b04e6209" />


## Resources

- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/fastmcp/fastmcp)
- [Cursor MCP Guide](https://cursor.sh/docs/mcp)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.vscode-mcp) 
