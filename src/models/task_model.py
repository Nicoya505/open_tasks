from config import Base

import datetime

from sqlalchemy import Column, Integer, String, DateTime

class TaskModel(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer(), primary_key=True)
    title = Column(String(50))
    description = Column(String(100))
    status = Column(String(10), default="pending")
    created_at = Column(DateTime(), default=datetime.datetime.now())