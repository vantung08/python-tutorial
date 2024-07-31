from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from ..dependencies import get_mongo_db, get_mongo_collection
from app.pydantic_schema import UserSchema
from app.crud import create_user

router = APIRouter(
    prefix="/users"
    )

@router.post("/")
async def add_user(user: UserSchema, collection: AsyncIOMotorCollection = Depends(get_mongo_collection)):
    try:
        created_user = await create_user(user, collection)
        return print(f"Document inserted with ID: {created_user['_id']}")
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