import logging
from fastapi import FastAPI
# from contextlib import asynccontextmanager
from app.api.main import api_router
# from app.initial_db import init_mongodb
from app import models
from app.database import engine

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

models.Base.metadata.create_all(bind=engine)
#-------------------
# @asynccontextmanager
# async def mongodb_lifespan(app: FastAPI):
#     # Startup actions
#     mongo_client = await init_mongodb()
#     print("Connected to MongoDB")
#     # Yield control back to the application
#     yield
#     # Shutdown actions
#     mongo_client.close()
#     print("Disconnected from MongoDB")

# app = FastAPI(lifespan=mongodb_lifespan)
#-----------------
app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}
