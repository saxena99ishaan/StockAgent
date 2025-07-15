
from google.adk.agents import Agent
from google.adk.tools import google_search  

StockNewsAgent = Agent(
    name="searchStockNewsAgent",
    model="gemini-2.0-flash",
    description="Creates the set of news that is relevant to a stock and may impact the stock price.",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    You are given a stock_symbol. You are to return all the latest news that is relevant to the stock price of the stock in Indian NSE market. Make sure that the news returned showcases the nature of the news and how it would impact the stock price in near future in your response properly. Remember to return the news properly and accurately.
    
    stock_symbol = {stockSymbol}
    """,
    tools=[google_search],
    output_key='stock_news'
)
