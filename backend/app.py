from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from routers.userRouter import router
from routers.authRouter import auth_router
from routers.menuRouter import menu_router
from routers.orderRouter import order_router
from middleware.errorHandler import ErrorHandler
from middleware.validationRequest import  validation_exception_handler
import os

app = FastAPI()
app.title = "API WILO"

origins = ["*"]

app.add_middleware(
    ErrorHandler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(auth_router)
app.include_router(menu_router)
app.include_router(order_router)

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, exc):
    return await validation_exception_handler(request, exc)
                                              