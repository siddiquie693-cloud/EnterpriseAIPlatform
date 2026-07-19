from ai.services.agent_state import AgentState
from ai.services.llm_service import LLMService

class SummarizerAgent:
    """
    Convert research notes into a concise summary.
    """

    def __call__(self, state: AgentState) -> AgentState:
        summary = LLMService.chat(
            prompt=(
                "Summarize the following research notes into a concise "
                "executive summary.\n\n"
                f"{state['research']}"
            )
        )

        state["summary"] = summary

        return state