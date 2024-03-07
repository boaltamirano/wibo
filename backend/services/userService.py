from fastapi.responses import JSONResponse
from fastapi import status
import bcrypt
from datetime import datetime
from config.db import get_database
from models.user import User, UserUpdate 
from utils.utils import json_response, user_token_response, hash_password, user_response
from bson import ObjectId

collection = get_database()["users"]

class UserService():
    
    def create_user(user:User):
        user.password = hash_password(user.password)
        user.created_at = int(datetime.utcnow().timestamp())        
        result = collection.insert_one(user.model_dump())
        id = result.inserted_id
        response_model = json_response( "User successfully registered", 201, True, body= user_token_response(id))
        return JSONResponse(status_code=status.HTTP_201_CREATED,content=response_model.model_dump())
    
    def get_users(page, limit):
        skipped = (page - 1) * limit
        users = [user_response(user) for user in collection.find().skip(skipped).limit(limit)]
        response_model = json_response( "Successful", 200, True, body= users)
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_model.model_dump())
    
    def get_user_by_id(id):
        user = collection.find_one({"_id": ObjectId(id)})
        if not user:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "User not found", 204, False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Successful", 200, True, body= user_response(user).model_dump()).model_dump())

    def update_user(id, user:UserUpdate):
        validation = collection.find_one({"_id": ObjectId(id)})
        if not user:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "User not found", 204, False).model_dump())    
        user.updated_at = int(datetime.utcnow().timestamp())
        collection.update_one({"_id": ObjectId(id)},{"$set": user.model_dump()})
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "The user has been modified").model_dump())
    
    def delete_user(id):
        user = collection.find_one({"_id": ObjectId(id)})
        if not user:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "User not found", 204, False).model_dump())    
        collection.delete_one({"_id": ObjectId(id)})
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "The user has been deleted").model_dump())
    
    def get_user(email):
        user = collection.find_one({"email": email})
        if not user:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=json_response( "Invalid user or password", 401, False).model_dump())    
        return User(**user).model_dump()

