from fastapi import APIRouter
from app.api_schema import UserIn, UserOut
from app.crud import create_user, find_user
from typing import Any

router = APIRouter(
    prefix="/users"
    )

@router.post("/", response_model=UserOut)
async def add_user(user: UserIn) -> Any:
    try:
        created_user = await create_user(user)
        print(f"Document inserted with ID: {created_user.id}")
        return created_user
    except Exception as e: # Required to refactor
        raise Exception(f"Unable to find the document due to the following error: {e}")

@router.get("/{user_name}", response_model=list[UserOut])
async def get_user(user_name: str) -> Any:
    try:
        return await find_user(user_name)
    except Exception as e:
        raise Exception(f"Unable to find the document due to the following error: {e}")