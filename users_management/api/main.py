from fastapi import APIRouter
from users_management.api.routers import users

api_router = APIRouter()

api_router.include_router(users.router)
# api_router.include_router(login.router)