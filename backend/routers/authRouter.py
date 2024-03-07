from fastapi import APIRouter
from controllers.authController import AuthController
from models.auth import Auth

auth_router = APIRouter()

@auth_router.post("/auth", tags=['Auth'])
def login(auth: Auth):
    return AuthController.authenticate_user(auth)