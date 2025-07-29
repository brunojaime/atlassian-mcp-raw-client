from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.streamable_http import streamablehttp_client
import asyncio
import os

 

async def initialize_atlassian_mcp_server(self, access_token):
    try:        
        server_params = StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "mcp-remote",
                "https://mcp.atlassian.com/v1/sse",
                #"--debug",
                "--transport", "sse-only",
                "--header",
                "Authorization:${AUTH_HEADER}"  
            ],
            env={"MCP_REMOTE_CONFIG_DIR":"/workspaces/atlassian-mcp-raw-client/auth_config"
                 }
        )
        # You can choose to pass the token over the connection, or tell the mcp-remote where to look it using MCP_REMOTE_CONFIG_DIR
        # By default it will look for the Authorization:${AUTH_HEADER}, if not found will go in to MCP_REMOTE_CONFIG_DIR.
        # If you dont set a MCP_REMOTE_CONFIG_DIR, it will create you one for you.
        transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        read_stream, write_stream = transport
        session = await self.exit_stack.enter_async_context(ClientSession(read_stream, write_stream))

        return session

    except asyncio.TimeoutError:
        self.logger.error("Connection to MCP server timed out.")
    except FileNotFoundError:
        self.logger.error("Failed to find 'npx' or 'mcp-remote' command. Is it installed?")
    except Exception as e:
        self.logger.exception(f"Unexpected error initializing Atlassian MCP server: {e}")
    
    return None