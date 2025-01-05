import logging
from fastapi import FastAPI
from auth_service.api.main import api_router
from auth_service import models
from auth_service.database import engine

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

models.Base.metadata.create_all(bind=engine)
auth_service = FastAPI()

auth_service.include_router(api_router)

@auth_service.get("/")
async def root():
    return {"message": "Hello Application"}