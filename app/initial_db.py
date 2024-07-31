from beanie import init_beanie
from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import UsersModel

async def init_mongodb():
    client = AsyncIOMotorClient(settings.mongodb_uri)
    db = client["python-tutorial-mongodb"]
    await init_beanie(database=db, document_models=[UsersModel])
