from fastapi import APIRouter
from pymongo import MongoClient

router = APIRouter()

uri = "mongodb://mongodb:27017"
client = MongoClient(uri)

@router.post("/users/{user_name}")
async def add_user(user_name, db: str = "mydb", cl: str = "user", age: int = 0, email: str = "TBD"):
    database = client[db]
    collection = database[cl]
    document = {
        "name": user_name,
        "age": age,
        "email": email
    }
    result = collection.insert_one(document)
    return print(f"Document inserted with ID: {result.inserted_id}")

@router.get("/users/{user_name}")
async def get_user(user_name, db: str = "mydb", cl: str = "user"):
    database = client.get_database(db)
    collection = database.get_collection(cl)
    user = collection.find_one({"name": user_name})
    return print(user)