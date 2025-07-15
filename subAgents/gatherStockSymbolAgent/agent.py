from google.adk.agents import Agent
from google.adk.tools import google_search  


stockSymbolAgent  = Agent(
    name="gatherStockSymbolAgent",
    model="gemini-2.0-flash",
    description="Searches google and returns the symbol for a stock in Indian NSE market.",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    You will be given a statement. Out of that figure out the stock and use the tool above to find the stock symbol for it. Remember to return only the symbol name that is used in indian stock market and NSE. Also just return the one word response and nothing else.
    """,
    tools=[google_search],
    output_key='stockSymbol'
)