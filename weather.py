from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(lcation:str)->str:
    """    
    Args:
        lcation (str): _description_

    Returns:
        str: _description_
    """
    return "weather in banglore is raniy"

if __name__=="__main__":
    mcp.run(transport="streamable-http")