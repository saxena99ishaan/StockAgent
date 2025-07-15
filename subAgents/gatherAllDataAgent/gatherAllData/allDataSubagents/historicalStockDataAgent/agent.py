from google.adk.agents import Agent
from .tools.tools import getStockAllData

historicalDataAgent = Agent(
    name="historicalStockDataAgent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - getStockAllData
    Use this tool to get the historical data for the stock by providing it the symbol given to you. Make sure only provide the NSE symbol to thr tool provided to you before running.
    
    symbol: {stockSymbol}
    """,

    tools=[getStockAllData],
    output_key='historical_data'
)
