"""
prompt-inferred filter models to assemble into a db aggregation/query
"""


from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field
from doc_metadata import Weekday, SourceType


class EmailMetadataFilter(BaseModel):
    """
    email filter model
    """

    sender_filter: List[Optional[str]] = Field(default_factory=list)
    recipient_group_filter: List[Optional[str]] = Field(default_factory=list)
    subject_filter: List[Optional[str]] = Field(default_factory=list)
    before_date_published: Optional[date]
    after_date_published: Optional[date]


class MenuMetadataFilter(BaseModel):
    """
    menu filter model
    """

    week_start_date_filter: List[Optional[date]] = Field(default_factory=list)
    days_of_week_filter: List[Optional[Weekday]] = Field(default_factory=list)


class PropsectusMetadataFilter(BaseModel):
    """
    prospectus filter model
    """

    school_filter: List[Optional[str]] = Field(default_factory=list)
    department_filter: List[Optional[str]] = Field(default_factory=list)


class DocumentMetadataFilter(BaseModel):
    """
    general filter model
    """

    document_id_filter: List[str] = Field(default_factory=list)
    source_type_filter: List[SourceType] = Field(default_factory=list)
    metadata_filters: List[
        EmailMetadataFilter | PropsectusMetadataFilter | MenuMetadataFilter
    ] = Field(default_factory=list)
