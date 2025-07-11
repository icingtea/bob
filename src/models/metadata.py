from datetime import date
from enum import Enum
from typing import Dict, List, Optional, Type, TypeAlias, Union
from pydantic import BaseModel, Field


class SourceType(str, Enum):
    EMAIL = "EMAIL"
    MENU = "MENU"
    PROSPECTUS = "PROSPECTUS"


# Do not use Field for recipients as that info is mandatory to initialize with.
# An email might not have any attached documents, but it will have recipients
class EmailMetadata(BaseModel):
    """
    Metadata definition for Email documents
    """

    sender: str
    recipients: List[str]
    subject: str
    date_published: date
    attached_documents: List[str] = Field(default_factory=List, description="List of attached document ids")


class MenuMetadata(BaseModel):
    """
    Metadata definition for Menu documents
    """

    week_start_date: Optional[date] = None


class PropsectusMetadata(BaseModel):
    """
    Metadata definition for Prospectus/Brochure documents
    """

    school: str
    department: str


GenericMetadata: TypeAlias = Union[EmailMetadata, MenuMetadata, PropsectusMetadata]
"""
A union type representing any of the possible metadata models depending on the source type
"""


class DocumentMetadata(BaseModel):
    """
    Generic metadata definition for all documents
    """

    document_id: str
    source_type: SourceType
    metadata: GenericMetadata


source_to_metadata_map: Dict[SourceType, Type[GenericMetadata]] = {
    SourceType.EMAIL: EmailMetadata,
    SourceType.MENU: MenuMetadata,
    SourceType.PROSPECTUS: PropsectusMetadata,
}
"""
Mapping from SourceType to its corresponging Metadata model
Useful for dynamically instantiating the correct Pydantic model based on SourceType 
"""
