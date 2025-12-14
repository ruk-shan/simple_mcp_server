from fastmcp import FastMCP

# Initialize the server
mcp = FastMCP("simple-server")

# Define a tool
# FastMCP automatically generates the schema from type hints and docstrings
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.run()