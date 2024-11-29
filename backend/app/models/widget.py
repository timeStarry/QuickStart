from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from backend.app.db.base import Base

class Widget(Base):
    __tablename__ = "widgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)  # clock, todo, pomodoro, etc
    title = Column(String)
    config = Column(JSON, default={})
    position = Column(JSON, default={"x": 0, "y": 0})
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now()) 