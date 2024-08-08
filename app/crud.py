from app.models import User
from app.schema import UserIn, UserInDB, UserUpdateIn, UserUpdateInDB
from app.core.security import get_password_hash
from fastapi import HTTPException
from pydantic import EmailStr
from app.core.security import verify_password
from uuid import UUID

async def create_user(schema_user: UserIn):
    hashed_password = get_password_hash(schema_user.password)
    In_DB_user = UserInDB(**schema_user.model_dump(), hashed_password=hashed_password)
    model_user = User(**In_DB_user.model_dump())
    new_user = await User.insert_one(model_user)
    return new_user

async def get_user_by_email(email: EmailStr) -> User:
    user = await User.find_one(User.email == email)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")
    return user

async def get_user_by_id(id: UUID) -> User:
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")
    return user

async def get_all_user() -> list[User]:
    users = await User.find().to_list()
    if not users:
        raise HTTPException(status_code=404, detail="User record not found!")
    return users

async def update_user(id: UUID, user_update: UserUpdateIn):
    if user_update.password is not None:
        hashed_password = get_password_hash(user_update.password)
        user_update = UserUpdateInDB(**user_update.model_dump(), hashed_password=hashed_password)
    filter_user_update = {k: v for k, v in user_update.model_dump().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in filter_user_update.items()
    }}
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")
    updated_user = await user.update(update_query)
    updated_user = await User.get(id)
    return updated_user

async def delete_user(id: UUID):
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")
    delete_user = await user.delete()
    return delete_user

async def authenticate_user(email: str, password: str) -> User:
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User record by email not found")
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return user