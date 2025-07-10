from typing import List
from pydantic import BaseModel

from models.metadata import DocumentMetadata


class Chunk(BaseModel):
    chunk_id: str
    text: str
    metadata: DocumentMetadata
    embeddings: List[float]
