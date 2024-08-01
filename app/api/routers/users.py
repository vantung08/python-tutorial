from fastapi import APIRouter
from app.api_schema import UserSchema
from app.crud import create_user, find_user

router = APIRouter(
    prefix="/users"
    )

@router.post("/")
async def add_user(user: UserSchema):
    try:
        created_user = await create_user(user)
        return print(f"Document inserted with ID: {created_user.id}")
    except Exception as e: # Required to refactor
        raise Exception(f"Unable to find the document due to the following error: {e}")

@router.get("/{user_name}")
async def get_user(user_name: str):
    try:
        user = await find_user(user_name)
        return print(user)
    except Exception as e:
        raise Exception(f"Unable to find the document due to the following error: {e}")