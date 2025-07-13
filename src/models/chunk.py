from typing import List
from pydantic import BaseModel

from models.metadata import DocumentMetadata, SourceType


class Chunk(BaseModel):
    """
    Atomic document definition
    """

    chunk_id: str
    source_type: SourceType
    metadata: DocumentMetadata
    text: str
    embeddings: List[float]
