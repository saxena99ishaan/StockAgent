from google.adk.agents import SequentialAgent
from .subAgents.gatherStockSymbolAgent import stockSymbolAgent
from .subAgents.gatherAllDataAgent.gatherAllData import gatherAllDataAgent
from .subAgents.resultSynthesizerAgent import resultAgent

root_agent = SequentialAgent(
    name="stockAgent",
    sub_agents=[stockSymbolAgent, gatherAllDataAgent, resultAgent],
    description="A pipeline that gathers the live and historical data for Indian NSE stocks and makes the analayis on it and returns when and how to invest on it"
)

