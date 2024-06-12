from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#user profile schema
class UserProfileSchema(BaseModel):
    id: int
    user_id: int
    bio: Optional[str]
    profile_picture: Optional[str]
    phone_number: Optional[str]
    role: str

    class Config:
        orm_mode = True

#agent schema
class AgentSchema(BaseModel):
    id: int
    user_id: int
    organisation_id: int

    class Config:
        orm_mode = True

#client schema
class ClientSchema(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    email: EmailStr
    date_created: str
    organisation_id: int

    class Config:
        orm_mode = True

#calendar schema
class CalendarEventSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_time: str
    end_time: str
    created_by_id: int
    attendee_ids: List[int]

    class Config:
        orm_mode = True

#document schema
class DocumentSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    uploaded_at: str
    uploaded_by_id: int
    file: str

    class Config:
        orm_mode = True

#meeting schema
class MeetingSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_time: str
    end_time: str
    created_by_id: int
    attendee_ids: List[int]
    google_meet_link: Optional[str]

    class Config:
        orm_mode = True

#task schema
class TaskSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: str
    assigned_to_id: int
    completed: bool

    class Config:
        orm_mode = True

#hr schema
class HRFileSchema(BaseModel):
    id: int
    user_id: int
    data: Any

    class Config:
        orm_mode = True

class HRFileCreateSchema(BaseModel):
    user_id: int
    data: Any

class HRFileUpdateSchema(BaseModel):
    data: Optional[Any]

#leave record schema
class LeaveRecordSchema(BaseModel):
    id: int
    user_id: int
    leave_type: str
    start_date: str
    end_date: str
    reason: Optional[str]

    class Config:
        orm_mode = True

class LeaveRecordCreateSchema(BaseModel):
    user_id: int
    leave_type: str
    start_date: str
    end_date: str
    reason: Optional[str] = ""

class LeaveRecordUpdateSchema(BaseModel):
    leave_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    reason: Optional[str]