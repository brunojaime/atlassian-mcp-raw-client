import asyncio
from asyncio.log import logger
from contextlib import AsyncExitStack
from dotenv import load_dotenv
from mcp_atlassian import initialize_atlassian_mcp_server
import os

load_dotenv()

atlassian_token = os.getenv("ATLASSIAN_TOKEN")

class Client():
    def __init__(self,exit_stack):
        self.exit_stack = exit_stack
        self.logger = logger

        
    async def connect_to_servers(self):
       
        session = await initialize_atlassian_mcp_server(self,atlassian_token)
        tools = await session.list_tools()
        print(tools)  
        
        
        result = await session.call_tool(
            #Choose the tool you want to call
            "atlassianUserInfo", 
            #Include the required parameters
            {}
        )
        print(result)
        


async def main():
    async with AsyncExitStack() as stack:
        client = Client(stack)
        await client.connect_to_servers()    
    
if __name__ == "__main__":
    asyncio.run(main())

