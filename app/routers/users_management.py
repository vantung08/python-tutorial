from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..dependencies import get_mongo_db
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(title="Name of the user", max_length=300)
    age: int = Field(default=None, gt=0, description="The price must be greater than zero")
    gender: str = None
    email: str | None = None

router = APIRouter(
    prefix="/users"
    )

@router.post("/")
async def add_user(user: User, collection_name: str = "users", mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db)):
    try:
        collection = mongo_db[collection_name]
        document = user.model_dump()
        result = await collection.insert_one(document)
        return print(f"Document inserted with ID: {result.inserted_id}")
    except Exception as e: # Required to refactor
        raise Exception("Unable to find the document due to the following error: ", e)

@router.get("/{user_name}")
async def get_user(user_name, collection_name: str = "users", mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db)):
    try:
        collection = mongo_db[collection_name]
        user = await collection.find_one({"name": user_name})
        return print(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to find the document due to the following error: {e}")