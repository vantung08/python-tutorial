from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import settings
from ..dependencies import get_mongo_client

router = APIRouter()

@router.post("/users/{user_name}")
async def add_user(user_name, db_name: str = "python-tutorial-mongodb", collection_name: str = "users",
                    age: int = 0, gender: str = "TBD", mongo_client: AsyncIOMotorClient = Depends(get_mongo_client)):
    try:
        db = mongo_client[db_name]
        collection = db[collection_name]
        document = {
            "name": user_name,
            "age": age,
            "gender": gender
        }
        result = await collection.insert_one(document)
        return print(f"Document inserted with ID: {result.inserted_id}")
    except Exception as e:
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