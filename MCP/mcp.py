# install: pip install "mcp[cli]"
from mcp.server.fastmcp import FastMCP

# 1) Server banao (koi sa bhi naam)
mcp = FastMCP("Demo Server")

# 2) Normal Python function ko @mcp.tool() se "TOOL" bana do
@mcp.tool()
def add(a: int, b: int) -> int:
    """Do number ko jodo."""   # ye line AI ko tool ka kaam samjhayegi
    return a + b

@mcp.tool()
def namaste(naam: str) -> str:
    """Diye gaye naam ko greeting bolo."""
    return f"Namaste {naam} 🙏"

# 3) Server chalao
mcp.run()

# Ab koi bhi MCP-wala AI app (Claude Desktop / Cursor / apna agent)
# iss server se jud kar add() aur namaste() tool khud use kar sakta hai!