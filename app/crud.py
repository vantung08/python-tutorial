from app.models import User
from app.schema import UserIn, UserInDB, UserUpdate
from app.core.security import get_password_hash
from beanie import PydanticObjectId
from fastapi import HTTPException

async def create_user(schema_user: UserIn):
    hashed_password = get_password_hash(schema_user.password)
    In_DB_user = UserInDB(**schema_user.model_dump(), hashed_password=hashed_password)
    model_user = User(**In_DB_user.model_dump())
    new_user = await User.insert_one(model_user)
    created_user = await User.find_one({"_id": new_user.id})
    return created_user

async def get_user(id: PydanticObjectId):
    return await User.get(id)

async def update_user(id: PydanticObjectId, user_update: UserUpdate):
    filter_user_update = {k: v for k, v in user_update.model_dump().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in filter_user_update.items()
    }}
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")
    await user.update(update_query)
    updated_user = await User.get(id)
    return updated_user
