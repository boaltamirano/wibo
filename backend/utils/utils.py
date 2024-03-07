from fastapi.responses import JSONResponse
from fastapi import status
from models.menu import Menu, MenuResponse
from models.order import Order, OrderResponse, OrderlDetailResponse
from models.response import Response
from config.db import get_database
from models.user import  UserToken, UserResponse, User
from bson import ObjectId
from datetime import datetime, timedelta
import jwt 
import bcrypt
import os

KEY = os.getenv("KEY")
TOKEN_EXPIRATION_MINUTES = os.getenv("TOKEN_EXPIRATION_MINUTES")
ALGORITHM = os.getenv("ALGORITHM")

def generate_token(email):
        payload = {
            "email": email,
            "exp": datetime.utcnow() + timedelta(minutes=int(TOKEN_EXPIRATION_MINUTES)),
        }
        token = jwt.encode(payload, KEY, algorithm=ALGORITHM)
        return token
def authenticate_user(email, password):
    # Buscar el usuario en la base de datos y verificar la contraseña
    user = get_database()["users"].find_one({"email": email})
    if user and user["password"] == password:
        return generate_token(email)
    return None

def user_token_response(id):
    user = get_database()['users'].find_one({"_id": ObjectId(id)})
    token = generate_token(user["email"])
    return UserToken(token= token, user=user_response(user)).model_dump()


def json_response(message, status = 200, ok = True, body = {}):
    return Response(ok=ok, message=message, body=body, status=status)

    
def hash_password(password) :
    hashed_password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    return hashed_password.decode("utf-8")

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def user_response(user: User):
    return UserResponse(
        id= str(user["_id"]), 
        name= user["name"], 
        lastname= user["lastname"], 
        age= user["age"], 
        email=user["email"], 
        created_at= user["created_at"], 
        updated_at= user["updated_at"]
    )

def menu_response(menu: Menu):
    return MenuResponse(
        id= str(menu["_id"]), 
        name= menu["name"], 
        price= menu["price"], 
        description= menu["description"], 
        image=menu["image"],
        rating= menu["rating"],
        created_at= menu["created_at"], 
        updated_at= menu["updated_at"]
    )

def order_response(order: Order):
    menus= []
    for m in order["menus"]:
        item = m
        item['menu']= menu_response(get_database()['menus'].find_one({"_id": ObjectId(item['menu'])}))
        menus.append(OrderlDetailResponse(**item)) 
    return OrderResponse(
        id= str(order["_id"]), 
        fecha= order["fecha"], 
        table= order["table"], 
        menu= menus,
        subtotal=order["subtotal"],
        total= order["total"],
        tip= order["tip"],
        state= order["state"],
        user= user_response(get_database()['users'].find_one({"_id": order["user"]})),
        created_at= order["created_at"], 
        updated_at= order["updated_at"]
    )

def validate_order(order: Order):
    order_save = order.model_dump()
    user = get_database()['users'].find_one({"_id": ObjectId(order_save['user'])})
    if not user:
        return None
    order_save['user'] = ObjectId(order.user)
    order_menu = order.menus
    menus = []
    for m in order_menu:
        item = m.model_dump()
        item['menu']= ObjectId(m.menu)
        menu = get_database()['menus'].find_one({"_id": ObjectId(item['menu'])})
        if not menu:
             return None
        menus.append(item)    
    order_save['menus'] = menus  
    return order_save