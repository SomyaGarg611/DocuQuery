from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
# from .session import Session
# from .chat import Chat

#Creating User Model
class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
    sessions = relationship("Session",back_populates="user")
    chats = relationship("Chat", back_populates="user")