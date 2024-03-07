import jwt
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request, status
from services.userService import UserService
from utils.utils import KEY, ALGORITHM, json_response

class AuthMiddleware(HTTPBearer):
    async def __call__(self, request: Request):
        try:
            token = request.headers["Authorization"].split(" ")[1]
            payload = jwt.decode(token, KEY, algorithms=[ALGORITHM])
            email = payload.get("email")
            user = UserService.get_user(email)
            if user:
                request.state.user = user
                response = await super().__call__(request) 
                return response
        except (jwt.exceptions.DecodeError, KeyError):
            pass

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= json_response( "Invalid or missing token",401).dict(),
        )