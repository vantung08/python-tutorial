from fastapi import APIRouter, status
from app.schema import UserIn, UserOut, UserUpdate
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
        raise Exception(f"Unable to create the document due to the following error: {e}")

@router.get("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user(id: PydanticObjectId) -> User:
    try:
        return await crud.get_user(id)
    except Exception as e:
        raise Exception(f"Unable to find the document due to the following error: {e}")
    
@router.put("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_user(id: PydanticObjectId, user_update: UserUpdate) -> User:
    try:
        updated_user = await crud.update_user(id, user_update)
        return updated_user
    except Exception as e:
        raise Exception(f"Unable to update the document due to the following error: {e}")