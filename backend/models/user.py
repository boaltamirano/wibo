from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class User(BaseModel):
    _id :       Optional[str] = "000000000000000000000000"
    name:       str = Field(min_length=3, max_length= 50)
    lastname:   str = Field(min_length=3, max_length= 50)
    age:        Optional[int] = Field(default=0, ge=18)
    email:      str = Field("example@example.com")
    password:   str 
    created_at: Optional [int] = 0
    updated_at: Optional [int] = 0

class UserUpdate(BaseModel):
    name:       str
    lastname:   str 
    age:        int
    email:      str
    created_at: int
    updated_at: Optional[int] = 0


class UserResponse(BaseModel):
    id :        str
    name:       str
    lastname:   str 
    age:        int
    email:      str
    created_at: int
    updated_at: int
    
class UserToken(BaseModel):
    token:      str
    user:       UserResponse 
