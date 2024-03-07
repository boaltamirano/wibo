from services.userService import UserService

class UserController:

    def create_user(user):
        return UserService.create_user(user)
    
    def get_users(page, limit):
        return UserService.get_users(page, limit)
    
    def get_user_by_id(id):
        return UserService.get_user_by_id(id)
    
    def update_user(id, user):
        return UserService.update_user(id, user)
    
    def delete_user(id):
        return UserService.delete_user(id)