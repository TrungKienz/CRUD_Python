from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str

class JobCreate(JobBase):
    begin_at: Optional[datetime] =  datetime.now
    end_at: Optional[datetime] = datetime.now
    content: Optional[str] = None


class JobUpdate(JobBase):
    status: bool

class JobResponce(JobBase):
    id: int
    status: bool

    class Config: 
        from_attributes = True