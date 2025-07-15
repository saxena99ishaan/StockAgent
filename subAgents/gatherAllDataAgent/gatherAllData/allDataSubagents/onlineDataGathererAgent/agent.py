
from google.adk.agents import ParallelAgent
from .onlineDataSubAgents.searchStockNewsAgent import StockNewsAgent
from .onlineDataSubAgents.searchStockDomainAgent import StockDomainAgent

onlineGathererAgent = ParallelAgent(
    name="onlineDataGathererAgent",
    sub_agents=[StockNewsAgent, StockDomainAgent],
)
