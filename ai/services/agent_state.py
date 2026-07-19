from typing import TypedDict

class AgentState(TypedDict):
    question: str
    document_id: int | None
    context: list
    research: str
    summary: str
    answer: str
    
    conversation_id: int | None

    conversation_history: str