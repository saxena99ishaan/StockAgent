
from google.adk.agents import Agent
from google.adk.tools import google_search  

StockDomainNewsAgent = Agent(
    name="searchStockDomainNewsAgent",
    model="gemini-2.0-flash",
    description="Creates the set of news that is relevant to a stock and may impact the stock price.",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    You are given a stock_symbol and it's domain industries as stock_domain. You are to return all the latest news stock domain and industry that is relevant to the stock price of the stock in Indian NSE market. Make sure that the news returned showcases the nature of the news and how it would impact the stock price in the stock domain in near future in your response properly. Remember to return the news properly and accurately. Keep most of the focus on the domain news rather thant the stock specific news.
    
    stock_symbol = {stockSymbol}
    stock_domain = {stockDomain}
    """,
    tools=[google_search],
    output_key='stock_domain_news'
)
