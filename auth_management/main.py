import logging
from fastapi import FastAPI
from auth_management.api.main import api_router
from auth_management import models
from auth_management.database import engine

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

models.Base.metadata.create_all(bind=engine)
auth_management = FastAPI()

auth_management.include_router(api_router)

@auth_management.get("/")
async def root():
    return {"message": "Hello Auth Service"}