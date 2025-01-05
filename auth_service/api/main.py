from fastapi import APIRouter
from auth_service.api.routers import login

api_router = APIRouter()

api_router.include_router(login.router)