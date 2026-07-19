from ai.models import Conversation
from ai.services.agent_state import AgentState

class HistoryAgent:
    """
    Load previous conversation messages.
    """

    def __call__(self, state: AgentState):
        conversation_id = state.get("conversation_id")

        if not conversation_id:
            state["conversation_history"] = ""
            return state
        
        try:
            conversation = Conversation.objects.get(
                id=conversation_id
            )

            history = []

            for message in conversation.messages.all().order_by("created_at"):
                history.append(
                    f"{message.role}: {message.content}"
                )

            state["conversation_history"] = "\n".join(history)

        except Conversation.DoesNotExist:
            state["conversation_history"] = ""
        return state            