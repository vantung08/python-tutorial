from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient

def get_mongo_client(request: Request) -> AsyncIOMotorClient:
    return request.app.mongo_client