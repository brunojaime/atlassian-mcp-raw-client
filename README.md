# Atlassian MCP Client – Project Overview

This project demonstrates how to connect a Python client to the Atlassian MCP (Model Context Protocol) server, discover available Atlassian tools, and invoke them using modern async Python patterns.

---

## Components

- **mcp_atlassian.py:**  
  Handles the connection and session initialization with the Atlassian MCP server.

- **call_atlassian_mcp_tool.py:**  
  Loads credentials, starts the client, lists available tools, and demonstrates tool invocation.

- **atlassians_tool_info.json:**  
  A catalog of all available Atlassian tools, including input and output schemas.  
  _No need to focus on individual tools for setup—this file is used for tool discovery and validation._

---

## Usage Flow

1. **Run the client:**  
   Use the following command to start the main script:
uv run call_atlassian_mcp_tool.py


2. **Token Handling:**

- The client will first try to find the Atlassian token using one of these strategies:
  - **Directly over the connection:**  
    Set the token as an environment variable (`Authorization:${AUTH_HEADER}`).
  - **Using a configuration directory:**  
    Set `MCP_REMOTE_CONFIG_DIR` so `mcp-remote` knows where to look for the token file.
  - **Fallback:**  
    If neither is set, `mcp-remote` will create a config directory for you automatically.

- **If the token is not set** (not present as `AUTH_HEADER` nor in `MCP_REMOTE_CONFIG_DIR`):  
  - In the CLI, you will be given a link to open in your browser to grant permissions to the MCP client.
  - After granting permissions, an auth token will be generated and saved automatically (in `MCP_REMOTE_CONFIG_DIR` if you set it).

- **Connection options**
 - You can choose to pass the token over the connection, or tell `mcp-remote` where to look for it using `MCP_REMOTE_CONFIG_DIR`.
 - By default, it will look for `Authorization:${AUTH_HEADER}`; if not found, it checks `MCP_REMOTE_CONFIG_DIR`.
 - If you don't set `MCP_REMOTE_CONFIG_DIR`, it will create one for you.

3. **List available Atlassian tools**  
All available tools are loaded from the JSON file. You do not need to configure tools individually.

4. **Invoke any Atlassian tool**  
After the client is authenticated, you can use any of the available tools as needed for your automation or workflow.

