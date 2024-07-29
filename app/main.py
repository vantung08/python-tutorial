import logging
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from .routers.users_management import router as users_router
from .core.config import settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@asynccontextmanager
async def mongodb_lifespan(app: FastAPI):
    # Startup actions
    app.mongo_client = AsyncIOMotorClient(settings.mongodb_uri)
    app.mongo_db = app.mongo_client["python-tutorial-mongodb"]
    print("Connected to MongoDB")
    # Yield control back to the application
    yield
    # Shutdown actions
    app.mongo_client.close()
    print("Disconnected from MongoDB")

app = FastAPI(lifespan=mongodb_lifespan)

app.include_router(users_router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}
