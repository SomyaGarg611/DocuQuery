from pydantic import BaseModel, EmailStr, Field

#Creating UserCreate 
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(...,min_length=4)


#Creating ShowUser 
class ShowUser(BaseModel):
    id : int
    email : EmailStr    

    class config():
        orm_mode = True
        from_attributes = True