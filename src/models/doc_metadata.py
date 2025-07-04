"""
metadata models to include in db chunks
"""

from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class Weekday(str, Enum):
    """
    weekday enum for menus
    """

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class SourceType(str, Enum):
    """
    document source enum
    """

    EMAIL = "EMAIL"
    MENU = "MENU"
    PROSPECTUS = "PROSPECTUS"


class EmailMetadata(BaseModel):
    """
    email information
    """

    sender: Optional[str] = None
    recipient_group: Optional[str] = None
    subject: Optional[str] = None
    date_published: Optional[date] = None
    attached_documents: Optional[List[str]] = None


class MenuMetadata(BaseModel):
    """
    menu information
    """

    week_start_date: Optional[date] = None
    day_of_week: Optional[Weekday] = None


class PropsectusMetadata(BaseModel):
    """
    prospectus information
    """

    school: Optional[str] = None
    department: Optional[str] = None


class DocumentMetadata(BaseModel):
    """
    general metadata model
    """

    document_id: str
    source_type: SourceType
    metadata: EmailMetadata | PropsectusMetadata | MenuMetadata
