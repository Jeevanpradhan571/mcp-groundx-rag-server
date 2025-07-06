import os
from dotenv import load_dotenv
from groundx import GroundX, Document
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp=FastMCP()
client = GroundX(api_key=os.getenv("GROUNDX_API_KEY"))

@mcp.tool()
def search_doc_for_rag_context(query:str)->str:
    """Search the groundx database for information"""
    
    response = client.search.content (
        id=19859,
        query=query,
        n=10,
    )

    return response.search.text

def main():
    print("About to start MCP server...")
    mcp.run()
    print("MCP server has stopped.")  # This will only print if the server stops

if __name__ == "__main__":
    main()


