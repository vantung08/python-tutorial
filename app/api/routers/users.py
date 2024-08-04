from fastapi import APIRouter, status
from app.schema import UserIn, UserOut, UserUpdateIn
from app.models import User
from app import crud
from beanie import PydanticObjectId

router = APIRouter(
    prefix="/users"
    )

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn) -> User:
    try:
        created_user = await crud.create_user(user)
        print(f"Document inserted with ID: {created_user.id}")
        return created_user
    except Exception as e: # Required to refactor
        raise Exception(f"Unable to create the user due to the following error: {e}")

@router.get("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user(id: PydanticObjectId) -> User:
    try:
        return await crud.get_user_by_id(id)
    except Exception as e:
        raise Exception(f"Unable to get the user due to the following error: {e}")
    
@router.get("/", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_all_user() -> list[User]:
    try:
        return await crud.get_all_user()
    except Exception as e:
        raise Exception(f"Unable to get the user due to the following error: {e}")
    
@router.put("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_user(id: PydanticObjectId, user_update: UserUpdateIn) -> User:
    try:
        updated_user = await crud.update_user(id, user_update)
        return updated_user
    except Exception as e:
        raise Exception(f"Unable to update the user due to the following error: {e}")
    
@router.delete("/{id}")
async def delete_user(id: PydanticObjectId):
    try:
        deleted_user = await crud.delete_user(id)
        return deleted_user.deleted_count
    except Exception as e:
        raise Exception(f"Unable to delete the user due to the following error: {e}")