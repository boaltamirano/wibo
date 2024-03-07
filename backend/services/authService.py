from fastapi.responses import JSONResponse
from fastapi import status
from models.auth import Auth
from utils.utils import json_response, user_token_response, verify_password
import os
from config.db import get_database

KEY = os.getenv("KEY")
TOKEN_EXPIRATION_MINUTES = os.getenv("TOKEN_EXPIRATION_MINUTES")
ALGORITHM = os.getenv("ALGORITHM")

class AuthService():
    def authenticate_user(auth: Auth):
        user = get_database()["users"].find_one({"email": auth.email})
        if len(user)<1 or  not verify_password(auth.password,user["password"]):
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=json_response( "Invalid user or password ", 401, False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK,content=json_response( "Successful", 200, True, body= user_token_response(str(user["_id"]))).model_dump())