from google.adk.agents import ParallelAgent
from .allDataSubagents.onlineDataGathererAgent import onlineGathererAgent
from .allDataSubagents.historicalStockDataAgent import historicalDataAgent

gatherAllDataAgent = ParallelAgent(
    name="gatherAllData",
    sub_agents=[onlineGathererAgent, historicalDataAgent],
)
