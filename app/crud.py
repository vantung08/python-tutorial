from motor.motor_asyncio import AsyncIOMotorCollection
from app.models import UsersModel
from app.pydantic_schema import UserSchema

async def create_user(schema_user: UserSchema, collection: AsyncIOMotorCollection):
    model_user = UsersModel(**schema_user.model_dump())
    new_user = await collection.insert_one(model_user.model_dump())
    created_user = await collection.find_one({"_id": new_user.inserted_id})
    return created_user