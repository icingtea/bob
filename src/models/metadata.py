from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import List, Optional 

class Weekday(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class EmailMetadata(BaseModel):
    document_id: str
    source_type: str = "email"
    sender: Optional[str] = None
    recipient_group: Optional[str] = None
    subject: Optional[str] = None
    date_published: Optional[date] = None
    attached_documents: Optional[List[str]] = None


class MenuMetadata(BaseModel):
    document_id: str
    source_type: str = "menu"
    week_start_date: Optional[date] = None
    day_of_week: Optional[Weekday] = None

# TODO: Make concrete implementation
class PropsectusMetadata(BaseModel):
    document_id: str
    source_type: str = "prospectus"
    school: Optional[str] = None
    department: Optional[str] = None