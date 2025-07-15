from google.adk.agents import SequentialAgent
from .stockDomainSubagents.searchStockDomainSegmentAgent import StockDomainSegmentAgent
from .stockDomainSubagents.searchStockDomainNewsAgent import StockDomainNewsAgent


StockDomainAgent = SequentialAgent(
    name="searchStockDomainAgent",
    sub_agents=[StockDomainSegmentAgent, StockDomainNewsAgent],
    description="A pipeline that gathers the live news for the domain of Indian NSE stocks and returns when and how to invest on it"
)

