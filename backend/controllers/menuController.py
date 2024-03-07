from services.menuService import MenuService

class MenuController:

    def create_menu(menu):
        return MenuService.create_menu(menu)
    
    def get_menus(page, limit):
        return MenuService.get_menus(page, limit)
    
    def get_menu_by_id(id):
        return MenuService.get_menu_by_id(id)
    
    def delete_menu(id):
        return MenuService.delete_menu(id)