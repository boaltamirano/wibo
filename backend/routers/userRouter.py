from fastapi import APIRouter, Depends, Query
from controllers.userController import UserController
from models.user import User, UserUpdate
from middleware.authMiddleware import AuthMiddleware

router = APIRouter()

@router.post("/users", tags=['Users'])
def create_user(user:User):
    return UserController.create_user(user)

@router.get("/users",tags=['Users'], dependencies=[Depends(AuthMiddleware())])
def get_users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    return  UserController.get_users(page ,limit)

@router.get("/users/{id}",tags=['Users'], dependencies=[Depends(AuthMiddleware())])
def get_user_by_id(id : str):
    return UserController.get_user_by_id(id)

@router.put("/users/{id}",tags=['Users'], dependencies=[Depends(AuthMiddleware())])
def update_user(id : str, user : UserUpdate):
    return UserController.update_user(id, user) 

@router.delete("/users/{id}",tags=['Users'], dependencies=[Depends(AuthMiddleware())])
def delete_user(id : str):
    return UserController.delete_user(id)
