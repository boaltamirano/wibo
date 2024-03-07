from pydantic import BaseModel, Field

class Auth(BaseModel):
    email:  str = Field("example@example.com")
    password:   str