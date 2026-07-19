from langgraph.graph import StateGraph, START, END

from ai.services.agent_state import AgentState

from ai.services.agents.retriever import RetrieverAgent
from ai.services.agents.researcher import ResearchAgent
from ai.services.agents.summarizer import SummarizerAgent
from ai.services.agents.answer import AnswerAgent

retriever = RetrieverAgent()
researcher = ResearchAgent()
summarizer = SummarizerAgent()
answer = AnswerAgent()

graph = StateGraph(AgentState)

graph.add_node("retriever", retriever)
graph.add_node("researcher", researcher)
graph.add_node("summarizer", summarizer)
graph.add_node("answer", answer)

graph.add_edge(START, "retriever")
graph.add_edge("retriever", "researcher")
graph.add_edge("researcher", "summarizer")
graph.add_edge("summarizer", "answer")
graph.add_edge("answer", END)

workflow = graph.compile()