from fastapi import APIRouter
from pymongo import MongoClient
from ..core.config import settings

router = APIRouter()

@router.post("/users/{user_name}")
async def add_user(user_name, database_name: str = "python-tutorial-mongodb", collection_name: str = "users", age: int = 0, gender: str = "TBD"):
    client = MongoClient(settings.mongodb_uri)
    try:
        database = client[database_name]
        collection = database[collection_name]
        document = {
            "name": user_name,
            "age": age,
            "gender": gender
        }
        result = collection.insert_one(document)
        client.close()
        return print(f"Document inserted with ID: {result.inserted_id}")
    except Exception as e:
        client.close()
        raise Exception("Unable to find the document due to the following error: ", e)

@router.get("/users/{user_name}")
async def get_user(user_name, database_name: str = "python-tutorial-mongodb", collection_name: str = "users"):
    client = MongoClient(settings.mongodb_uri)
    try:
        database = client.get_database(database_name)
        collection = database.get_collection(collection_name)
        user = collection.find_one({"name": user_name})
        client.close()
        return print(user)
    except Exception as e:
        client.close()
        raise Exception("Unable to find the document due to the following error: ", e)