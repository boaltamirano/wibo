from fastapi import APIRouter, Depends, Query
from controllers.orderController import OrderController
from models.order import Order
from middleware.authMiddleware import AuthMiddleware

order_router = APIRouter()

@order_router.post("/orders", tags=['Orders'], dependencies=[Depends(AuthMiddleware())])
def create_order(order:Order):
    return OrderController.create_order(order)

@order_router.get("/orders",tags=['Orders'], dependencies=[Depends(AuthMiddleware())])
def get_orders(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    return  OrderController.get_orders(page ,limit)

@order_router.get("/orders/{id}",tags=['Orders'], dependencies=[Depends(AuthMiddleware())])
def get_order_by_id(id : str):
    return OrderController.get_order_by_id(id)

@order_router.get("/orders/user/{id}",tags=['Orders'], dependencies=[Depends(AuthMiddleware())])
def get_order_by_user(user_id : str, page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    return OrderController.get_order_by_user(user_id, page, limit )

@order_router.delete("/orders/{id}",tags=['Orders'], dependencies=[Depends(AuthMiddleware())])
def delete_order(id : str):
    return OrderController.delete_order(id)
