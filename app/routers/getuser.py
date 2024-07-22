from fastapi import APIRouter
from pymongo import MongoClient

router = APIRouter()

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

@router.get("/users/{user_name}")
async def get_user(user_name, db: str = "mydb", cl: str = "user"):
    database = client.get_database(db)
    collection = database.get_collection(cl)
    user = collection.find_one({"name": "Tony"})
    return print(user)