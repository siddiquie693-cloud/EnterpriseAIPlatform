from ai.services.agent_state import AgentState
from ai.services.llm_service import LLMService

class ResearchAgent:
    """
    converts retrieved chunks into concise research notes.
    """

    def __call__(self, state: AgentState) -> AgentState:
        context = "\n\n".join(
            chunk["text"]
            for chunk in state["context"]
        )

        research = LLMService.answer_question(
            document=context,
            question=(
                "Read the following context and prepare research notes."
                "Do not answer the user's question yet. "
                "Extract only the important facts."
            ),
        )

        state["research"] = research

        return state