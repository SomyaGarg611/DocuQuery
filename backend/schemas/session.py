from pydantic import BaseModel
from datetime import datetime

#Creating CreateSession
class CreateSession(BaseModel):
    user_id : int

#creating ShowSession 
class ShowSession(BaseModel):
    id : int
    user_id : int
    created_at : datetime
      
    class config():
        orm_mode = True
        from_attributes = True