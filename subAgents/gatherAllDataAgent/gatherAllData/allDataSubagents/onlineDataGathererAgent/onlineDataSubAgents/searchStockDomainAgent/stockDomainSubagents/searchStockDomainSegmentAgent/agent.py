
from google.adk.agents import Agent
from google.adk.tools import google_search  

StockDomainSegmentAgent = Agent(
    name="searchStockDomainSegmentAgent",
    model="gemini-2.0-flash",
    description="Searches the domain of a stock symbol from Indian NSE market",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    You are given a stock_symbol. You are to return the domain for Indian NSE stock market symbol. The stock can be a single or multiple domain stock. The domain can be like: Food industry, Aerospace Industry, Defence Industry, Finance Industry, etc. Return all the domains the stock symbol falls into
    
    stock_symbol = {stockSymbol}
    """,
    tools=[google_search],
    output_key='stockDomain'
)
