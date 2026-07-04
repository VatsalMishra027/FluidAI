from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

# API Models
class AgentRequest(BaseModel):
    request: str = Field(..., description="The user's natural language request to process.")

class AgentResponse(BaseModel):
    status: str
    message: str
    document_path: str
    plan: List[str]

# Agent State Models
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    """
    State for the LangGraph agent workflow.
    """
    request: str
    plan: List[str]
    draft_content: Dict[str, str]
    current_section_index: int
    feedback: str
    reflection_passed: bool
    document_path: str
    error: str
