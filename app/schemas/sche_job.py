from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobItem(BaseModel):
    title: str
    begin_at: datetime
    end_at: datetime
    status: Optional[bool] = False
    content: Optional[str] = None
    