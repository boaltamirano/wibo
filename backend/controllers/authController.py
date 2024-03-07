from services.authService import AuthService

class AuthController:

    def authenticate_user(auth):
        return AuthService.authenticate_user(auth)