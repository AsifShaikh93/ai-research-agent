from typing import List, TypedDict, Optional

class AgentState(TypedDict):
    query: str
    urls: Optional[List[str]]
    documents: Optional[List[str]]
    context: Optional[str]
    report: Optional[str]