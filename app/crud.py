from app.models import User
from app.pydantic_schema import UserSchema

async def create_user(schema_user: UserSchema):
    model_user = User(**schema_user.model_dump())
    new_user = await User.insert_one(model_user)
    created_user = await User.find_one({"_id": new_user.id})
    return created_user

async def find_user(user_name: str):
    return await User.find({"name": user_name}).to_list()