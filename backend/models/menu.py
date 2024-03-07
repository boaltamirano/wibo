from pydantic import BaseModel, Field
from typing import Optional

class Menu(BaseModel):
    _id :           Optional[str] = "000000000000000000000000"
    name:           str = Field(min_length=3, max_length= 50)
    price:          float 
    description:    Optional[str] = Field(min_length=3, max_length= 250)
    image:          Optional[bytes] = None
    rating:         Optional [int] = 0
    created_at:     Optional [int] = 0
    updated_at:     Optional [int] = 0

class MenuResponse(BaseModel):
    id :            Optional[str] = "000000000000000000000000"
    name:           str = Field(min_length=3, max_length= 50)
    price:          float 
    description:    Optional[str] = Field(min_length=3, max_length= 250)
    image:          Optional[str] 
    rating:         Optional [int] = 0
    created_at:     Optional [int] = 0
    updated_at:     Optional [int] = 0