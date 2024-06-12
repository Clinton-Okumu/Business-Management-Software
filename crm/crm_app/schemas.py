from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserSchema(BaseModel):
    id: int
    username: str
    email: str


class AdminProfileSchema(BaseModel):
    user: UserSchema
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    phone_number: Optional[str] = None
    role: str


class CustomerProfileSchema(BaseModel):
    user: UserSchema
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    phone_number: Optional[str] = None


class CalendarEventSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    created_by: UserSchema
    attendees: List[UserSchema]


class DocumentSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    uploaded_at: datetime
    uploaded_by: UserSchema
    file: str


class MeetingSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    created_by: UserSchema
    attendees: List[UserSchema]
    google_meet_link: Optional[str] = None


class TaskSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: datetime
    assigned_to: UserSchema
    completed: bool


class DepartmentSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class RoleSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    department: DepartmentSchema
    users: List[UserSchema]
