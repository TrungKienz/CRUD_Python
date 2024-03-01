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
    id: int 
    status: bool
    content: str
    end_at: datetime 
    class Config: 
        from_attributes = True

class JobResponce(JobBase):
    id: int
    status: bool

    class Config: 
        from_attributes = True

class JobDetail(JobBase):
    id: int
    title: str
    status: bool

    class Config:
        from_attributes = True