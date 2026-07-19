from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    """
    Shared state passed between all Langgraph agents.
    """

    # User input 
    question: str

    # Optional document restriction 
    document_id: Optional[int]

    # Retrieved chunks 
    context: List[dict]

    # Research notes
    research: str

    # Generate summary 
    summary: str

    # Final answer 
    answer: str
    