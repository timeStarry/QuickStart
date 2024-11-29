from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

class Todo(TodoBase):
    id: int
    user_id: int
    is_completed: bool 