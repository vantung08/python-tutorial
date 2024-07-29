from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..dependencies import get_mongo_client
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(title="Name of the user", max_length=300)
    age: int = Field(default=None, gt=0, description="The price must be greater than zero")
    gender: str = None
    email: str | None = None

router = APIRouter()

@router.post("/users/")
async def add_user(user: User, db_name: str = "python-tutorial-mongodb", collection_name: str = "users", mongo_client: AsyncIOMotorClient = Depends(get_mongo_client)):
    try:
        db = mongo_client[db_name]
        collection = db[collection_name]
        document = user.model_dump()
        result = await collection.insert_one(document)
        return print(f"Document inserted with ID: {result.inserted_id}")
    except Exception as e: # Required to refactor
        raise Exception("Unable to find the document due to the following error: ", e)

@router.get("/users/{user_name}")
async def get_user(user_name, db_name: str = "python-tutorial-mongodb", collection_name: str = "users",
                    mongo_client: AsyncIOMotorClient = Depends(get_mongo_client)):
    try:
        db = mongo_client[db_name]
        collection = db[collection_name]
        user = await collection.find_one({"name": user_name})
        return print(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to find the document due to the following error: {e}")