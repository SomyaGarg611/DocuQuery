from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from .session import Session
from .user import User

#Creating Chat Model
class Chat(Base):
    id = Column(Integer, index=True,primary_key=True)
    user_id=Column(Integer, ForeignKey("user.id") )
    session_id=Column(Integer, ForeignKey("session.id"))
    input_query = Column(String)
    output_query = Column()
    chatTimestamp = Column(DateTime,default=datetime.now())
    format = Column(String)
    session = relationship("Session", back_populates="chats")
    user = relationship("User", back_populates="chats")


    

    
    