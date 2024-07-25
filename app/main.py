import logging
from fastapi import FastAPI
from app.routers import greeting, users_management

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(greeting.router)
app.include_router(users_management.router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}
