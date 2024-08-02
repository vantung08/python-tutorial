from fastapi import APIRouter, status
from app.schema import UserIn, UserOut
from app.models import User
from app.crud import create_user, find_user

router = APIRouter(
    prefix="/users"
    )

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserIn) -> User:
    try:
        created_user = await create_user(user)
        print(f"Document inserted with ID: {created_user.id}")
        return created_user
    except Exception as e: # Required to refactor
        raise Exception(f"Unable to find the document due to the following error: {e}")

@router.get("/{user_name}", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_user(user_name: str) -> list[User]:
    try:
        return await find_user(user_name)
    except Exception as e:
        raise Exception(f"Unable to find the document due to the following error: {e}")