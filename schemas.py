from pydantic import BaseModel
from typing import Optional
from datetime import datetime
    

class MemberBase(BaseModel):
    name: str
    email:str
    membership_type: Optional[str] = None

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email:Optional[str]=None
    membership_type: Optional[str] = None

class Member(MemberBase):
    member_id: int
    registration_date: datetime

    class Config:
        from_attributes = True 
        json_encoders = { datetime: lambda v: v.isoformat(),} 

class EventBase(BaseModel):
    title: str
    member_id:int 
    location:str
    description: str
    

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    member_id: Optional[int] = None
    location: Optional[str] = None
    description: Optional[str] = None


class Event(EventBase):
    event_id: int
    

    class Config:
        from_attributes = True
        json_encoders = { datetime: lambda v: v.isoformat(),}
