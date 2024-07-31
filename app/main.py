import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.main import api_router
from app.initial_db import init_mongodb

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@asynccontextmanager
async def mongodb_lifespan(app: FastAPI):
    # Startup actions
    await init_mongodb()
    print("Connected to MongoDB")
    # Yield control back to the application
    yield
    # Shutdown actions
    app.mongo_client.close()
    print("Disconnected from MongoDB")

app = FastAPI(lifespan=mongodb_lifespan)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}
