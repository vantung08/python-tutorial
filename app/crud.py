from app.models import User
from app.schema import UserIn, UserInDB
from app.core.security import get_password_hash

async def create_user(schema_user: UserIn):
    hashed_password = get_password_hash(schema_user.password)
    In_DB_user = UserInDB(**schema_user.model_dump(), hashed_password=hashed_password)
    model_user = User(**In_DB_user.model_dump())
    new_user = await User.insert_one(model_user)
    created_user = await User.find_one({"_id": new_user.id})
    return created_user

async def find_user(user_name: str):
    return await User.find({"username": user_name}).to_list()