"""
graph state model
"""

from typing import Annotated, Optional, List
from pydantic import BaseModel
from doc_metadata import DocumentMetadata, SourceType
from langgraph.graph.message import add_messages


class State(BaseModel):
    """
    state def pls change if u need
    """

    question: Optional[str]
    chunk_filter: SourceType
    metadata_filter: DocumentMetadata
    retrieved_context: List[str]
    recent_context: str
    chat_memory: Annotated[List, add_messages]
    error: Optional[str]
    chat_response: Optional[str]
