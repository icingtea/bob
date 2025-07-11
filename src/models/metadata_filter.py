from datetime import date
from typing import List, Optional, TypeAlias, Union
from pydantic import BaseModel, Field

from models.metadata import SourceType


class EmailMetadataFilter(BaseModel):
    """
    Filter model for Email metadata
    """

    sender_filter: List[str] = Field(default_factory=List)
    recipient_filter: List[str] = Field(default_factory=List)
    subject_filter: List[str] = Field(default_factory=List)
    before_date_published: Optional[date] = None
    after_date_published: Optional[date] = None


# There is nothing else to be filtering over
# Therefore, a week_start_date_filter is mandatory
class MenuMetadataFilter(BaseModel):
    """
    Filter model for Menu metadata
    """

    week_start_date_filter: date


class ProspectusMetadataFilter(BaseModel):
    """
    Filter model for Prospectus/Brochure metadata
    """

    school_filter: List[str] = Field(default_factory=List)
    department_filter: List[str] = Field(default_factory=List)


GenericMetadataFilter: TypeAlias = Union[EmailMetadataFilter, MenuMetadataFilter, ProspectusMetadataFilter]
"""
A union type representing any of the possible metadata filters based on user request inference  
"""


class DocumentMetadataFilter(BaseModel):
    """
    Generic metadata filter definition for all requests
    """

    document_id_filter: List[str] = Field(default_factory=List)
    source_type_filter: List[SourceType] = Field(default_factory=List)
    metadata_filter: List[GenericMetadataFilter] = Field(default_factory=List)
