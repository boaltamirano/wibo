from fastapi import APIRouter, Depends, Query
from controllers.menuController import MenuController
from models.menu import Menu
from middleware.authMiddleware import AuthMiddleware

menu_router = APIRouter()

@menu_router.post("/menus", tags=['Menus'], dependencies=[Depends(AuthMiddleware())])
def create_menu(menu:Menu):
    return MenuController.create_menu(menu)

@menu_router.get("/menus",tags=['Menus'], dependencies=[Depends(AuthMiddleware())])
def get_menus(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    return  MenuController.get_menus(page ,limit)

@menu_router.get("/menus/{id}",tags=['Menus'], dependencies=[Depends(AuthMiddleware())])
def get_menu_by_id(id : str):
    return MenuController.get_menu_by_id(id)

@menu_router.delete("/menus/{id}",tags=['Menus'], dependencies=[Depends(AuthMiddleware())])
def delete_menu(id : str):
    return MenuController.delete_menu(id)
