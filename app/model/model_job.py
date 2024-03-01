from app.model.model_base import BareBaseModel
from sqlalchemy import Column, DateTime, String, Boolean
from datetime import datetime

class Job(BareBaseModel):
    __tablename__ = "todolist"

    title = Column(String)
    begin_at = Column(DateTime, default=datetime.now())
    end_at = Column(DateTime)
    status = Column(Boolean, default=False)
    content = Column(String)