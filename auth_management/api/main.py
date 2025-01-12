from fastapi import APIRouter
from auth_management.api.routers import signup, login

api_router = APIRouter()

api_router.include_router(signup.router)
api_router.include_router(login.router)