from fastapi.responses import JSONResponse
from fastapi import status
import bcrypt
from datetime import datetime
from config.db import get_database
from models.menu import Menu
from utils.utils import json_response, menu_response
from bson import ObjectId

collection = get_database()["menus"]

class MenuService():
    def create_menu(menu:Menu):
        menu.created_at = int(datetime.utcnow().timestamp())
        collection.insert_one(menu.model_dump())     
        return JSONResponse(status_code=status.HTTP_201_CREATED,content=json_response( "Menu successfully registered", 201).model_dump())
    
    def get_menus(page, limit):
        skipped = (page - 1) * limit
        menus = [menu_response(menu) for menu in collection.find().skip(skipped).limit(limit)]
        response_model = json_response( "Successful", 200, True, body= menus)
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_model.model_dump())
    
    def get_menu_by_id(id):
        menu = collection.find_one({"_id": ObjectId(id)})
        if not menu:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Menu not found", 204, False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Successful", 200, True, body= menu_response(menu).model_dump()).model_dump())

    
    def delete_menu(id):
        menu = collection.find_one({"_id": ObjectId(id)})
        if not menu:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Menu not found", 204, False).model_dump())    
        collection.delete_one({"_id": ObjectId(id)})
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "The menu has been deleted").model_dump())
    