from langgraph.graph import StateGraph, START, END

from ai.services.agent_state import AgentState

from ai.services.agents.history import HistoryAgent
from ai.services.agents.retriever import RetrieverAgent
from ai.services.agents.researcher import ResearchAgent
from ai.services.agents.summarizer import SummarizerAgent
from ai.services.agents.answer import AnswerAgent
def build_workflow():
    history = HistoryAgent()
    retriever = RetrieverAgent()
    researcher = ResearchAgent()
    summarizer = SummarizerAgent()
    answer = AnswerAgent()

    graph = StateGraph(AgentState)

    graph.add_node("history", history)
    graph.add_node("retriever", retriever)
    graph.add_node("researcher", researcher)
    graph.add_node("summarizer", summarizer)
    graph.add_node("answer", answer)

    graph.add_edge(START, "history")
    graph.add_edge("history", "retriever")
    graph.add_edge("retriever", "researcher")
    graph.add_edge("researcher", "summarizer")
    graph.add_edge("summarizer", "answer")
    graph.add_edge("answer", END)

    return graph.compile()