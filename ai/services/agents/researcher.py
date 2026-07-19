from ai.services.agent_state import AgentState
from ai.services.llm_service import LLMService

class ResearchAgent:
    """
    Extract important information from retrieved context.
    """

    def __call__(self, state: AgentState) -> AgentState:

        context = "\n\n".join(
            item["text"]
            for item in state["context"]
        )

        research = LLMService.chat(
            prompt=f"""
You are an AI Research Assistant.

Previous Conversation:
{state["conversation_history"]}

Retrieved Context:
{context}

Current User Question:
{state["question"]}

Instructions:
- Read the retrieved context carefully.
- Consider the previous conversation to understand follow-up questions.
- Extract only the important facts needed to answer the user's question.
- Do not make up information.
- Keep the research factual and well organized.
"""
        )

        state["research"] = research

        return state