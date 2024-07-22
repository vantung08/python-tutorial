import logging
from fastapi import FastAPI
from app.routers import greeting, adduser, getuser


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(greeting.router)
app.include_router(adduser.router)
app.include_router(getuser.router)

@app.get("/")
async def root():
    return {"message": "Hello Application"}
