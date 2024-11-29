from typing import Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime

class WidgetBase(BaseModel):
    type: str
    title: Optional[str] = None
    config: Dict[str, Any] = {}
    position: Dict[str, int] = {"x": 0, "y": 0}

class WidgetCreate(WidgetBase):
    pass

class WidgetUpdate(WidgetBase):
    type: Optional[str] = None

class Widget(WidgetBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 