from pydantic import BaseModel
from typing import Optional

#Creating the CreateChat
class CreateChat(BaseModel):
    user_id : int
    session_id : int
    input_query : str
    format: Optional[str] = None


# class ShowChat(BaseModel):
#     id : int
#     user_id : int
#     session_id : int
#     chatTimestamp : datetime
#     input_query : str
#     output_query : str
#     format : Optional[str]
      
    # class Config:
    #     orm_mode = True  
    #     from_attributes = True  


