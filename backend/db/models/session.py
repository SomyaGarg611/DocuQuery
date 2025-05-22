from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base
# from .user import User
# from .chat import Chat

#Creating Session Model
class Session(Base):
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer, ForeignKey("user.id"))
    user=relationship("User", back_populates="sessions")
    created_at= Column(DateTime,default=datetime.now)
    chats = relationship("Chat", back_populates="session")
    # is_active=Column(Boolean,default=False)

