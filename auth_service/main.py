import logging
from fastapi import FastAPI
from auth_service.api.main import api_router
from auth_service import models
from auth_service.database import engine

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}