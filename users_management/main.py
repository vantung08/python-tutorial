import logging
from fastapi import FastAPI
from users_management.api.main import api_router
from users_management import models
from users_management.database import engine

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
users_management = FastAPI()

users_management.include_router(api_router)

@users_management.get("/")
async def root():
    return {"message": "Hello Application"}
