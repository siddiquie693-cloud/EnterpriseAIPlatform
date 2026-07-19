from ai.services.agent_state import AgentState
from ai.services.llm_service import LLMService

class AnswerAgent:
    """
    Generate the final answer using the summary.
    """

    def __call__(self, state: AgentState) -> AgentState:
        answer = LLMService.chat(
            prompt=
                f"""
You are an Enterprise AI Assistant. 

Previous Conversation:
{state["conversation_history"]}

Document Summary:
{state["summary"]}

Current User Question:
{state["question"]}

Instructions:
- Use the previous conversation whenever it is relevant.
- If the current question refers to earlier messages (for example: "it", "that", "explain more", "give another example"), use the conversation history to understand the reference.
- Answer using the document summary.
- If the answer is not available in the summary, politely say so.
- Keep the answer concise and accurate.
"""
        )

        state["answer"] = answer

        return state



