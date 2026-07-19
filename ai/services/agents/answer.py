from ai.services.agent_state import AgentState
from ai.services.llm_service import LLMService

class AnswerAgent:
    """
    Generate the final answer using the summary.
    """

    def __call__(self, state: AgentState) -> AgentState:
        answer = LLMService.chat(
            prompt=(
                f"""
You are an Enterprise AI Assistant. 

Use the following summary to answer the user's question accurately. 

Summary:
{state["summary"]}

Question:
{state["question"]}

Instructions:
- Answer only from the summary. 
- Be concise. 
- If the answer is not available, say so politely. 
"""
            )
        )

        state["answer"] = answer

        return state