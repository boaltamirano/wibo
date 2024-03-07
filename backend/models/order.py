from pydantic import BaseModel, Field
from models.menu import MenuResponse
from typing import Optional, List
from bson import ObjectId
from models.user import UserResponse

class OrderDetail(BaseModel):
    menu:       str
    amount:     int
    subtotal:   float

class Order(BaseModel):
    _id :       Optional[str] = "000000000000000000000000"
    fecha:      Optional [int] = 0
    table:      Optional [int] = 1
    menus:      List[OrderDetail] = Field(default_factory=list)
    subtotal:   float
    total:      float
    tip:        Optional [float] = 0.0
    state:      Optional[str] = 'Pendiente'
    user:       str    
    created_at: Optional [int] = 0
    updated_at: Optional [int] = 0


class OrderlDetailResponse(BaseModel):
    menu:       MenuResponse
    amount:     int
    subtotal:   float

class OrderResponse(BaseModel):
    id :        str
    fecha:      Optional [int] = 0
    table:      Optional [int] = 1 
    menu:       List[OrderlDetailResponse] = Field(default_factory=list)
    subtotal:   float
    total:      float
    tip:        Optional [float] = 0.0
    state:      str
    user:       UserResponse
    created_at: Optional [int] = 0
    updated_at: Optional [int] = 0