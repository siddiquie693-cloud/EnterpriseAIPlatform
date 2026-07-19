from ai.services.agents.state import AgentState
from search.services.hybrid_search import HybridSearchService

class RetrieverAgent:
    """
    LangGraph Retriever Agent.

    Uses the existing Hybrid Search service to retrieve
    the most relevant document chunks.
    """

    def __init__(self):
        self.search_service = HybridSearchService()


    def __call__(self, state: AgentState) -> AgentState:
        results = self.search_service.search(
            query=state["question"],
            document_id=state.get("document_id"),
            top_k=5,
        )

        # HybridsearchService returns {"result": [...]}
        state["context"] = results.get("results", [])

        return state