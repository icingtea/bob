"""
general chunk/chunk helper models to pass into db
"""

from typing import List
from pydantic import BaseModel
from doc_metadata import DocumentMetadata


class Chunk(BaseModel):
    """
    chunk model
    """

    chunk_id: str
    metadata: DocumentMetadata
    text: str
    embeddings: List[float]
