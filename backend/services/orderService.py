from fastapi.responses import JSONResponse
from fastapi import status
import bcrypt
from datetime import datetime
from config.db import get_database
from models.order import Order
from utils.utils import json_response, order_response, validate_order
from bson import ObjectId

collection = get_database()["orders"]

class OrderService():
    def create_order(order:Order):
        order.created_at = int(datetime.utcnow().timestamp())
        order_save = validate_order(order)
        if not order_save:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Id user or menu not found", 204, False).model_dump())
        collection.insert_one(order_save)     
        return JSONResponse(status_code=status.HTTP_201_CREATED,content=json_response( "Order successfully registered", 201).model_dump())
    
    def get_orders(page, limit):
        skipped = (page - 1) * limit
        orders = [order_response(order) for order in collection.find().skip(skipped).limit(limit)]
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Successful", 200, True, body= orders).model_dump())
    
    def get_order_by_id(id):
        order = collection.find_one({"_id": ObjectId(id)})
        if not order:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Order not found", 204, False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Successful", 200, True, body= order_response(order).model_dump()).model_dump())

    def get_order_by_user(user_id, page, limit):
        skipped = (page - 1) * limit
        orders = [order_response(order) for order in collection.find({"user": ObjectId(user_id)}).skip(skipped).limit(limit)]
        if not orders:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Orders to user not found", 204, False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Successful", 200, True, body= orders).model_dump())

    
    def delete_order(id):
        order = collection.find_one({"_id": ObjectId(id)})
        if not order:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Order not found", 204, False).model_dump())    
        collection.delete_one({"_id": ObjectId(id)})
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "The order has been deleted").model_dump())