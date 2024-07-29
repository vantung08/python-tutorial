from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

def get_mongo_client(request: Request) -> AsyncIOMotorClient:
    return request.app.mongo_client

def get_mongo_db(request: Request) -> AsyncIOMotorDatabase:
    return request.app.mongo_db