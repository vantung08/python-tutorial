from app.database import SessionLocal
from fastapi import APIRouter, status, Depends
from app import crud
from app.schema import UserIn, UserOut
from app.models import User
from sqlalchemy.orm import Session
from uuid import UUID

router = APIRouter(
    prefix="/users"
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserIn, db: Session = Depends(get_db)) -> User:
    try:
        created_user = crud.create_user(db=db, schema_user=user)
        return created_user
    except Exception as e: # Required to refactor
        raise Exception(f"Unable to create the user due to the following error: {e}")

@router.get("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
def get_user(id: UUID, db: Session = Depends(get_db)) -> User:
    try:
        return crud.get_user_by_id(db=db, id=id)
    except Exception as e:
        raise Exception(f"Unable to get the user due to the following error: {e}")











# from fastapi import APIRouter, status, Depends
# from app.schema import UserIn, UserOut, UserUpdateIn
# from app.models import User
# from app import crud
# from uuid import UUID
# from typing import Annotated
# from app.api.deps import get_current_active_user

# router = APIRouter(
#     prefix="/users",
#     dependencies=[Depends(get_current_active_user)]
#     )

# @router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserIn) -> User:
#     try:
#         created_user = await crud.create_user(user)
#         return created_user
#     except Exception as e: # Required to refactor
#         raise Exception(f"Unable to create the user due to the following error: {e}")
    
# @router.get("/me")
# async def get_user_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
#     return current_user

# @router.get("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
# async def get_user(id: UUID) -> User:
#     try:
#         return await crud.get_user_by_id(id)
#     except Exception as e:
#         raise Exception(f"Unable to get the user due to the following error: {e}")
    
# @router.get("/", response_model=list[UserOut], status_code=status.HTTP_200_OK)
# async def get_all_user() -> list[User]:
#     try:
#         return await crud.get_all_user()
#     except Exception as e:
#         raise Exception(f"Unable to get the user due to the following error: {e}")
    
# @router.put("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
# async def update_user(id: UUID, user_update: UserUpdateIn) -> User:
#     try:
#         updated_user = await crud.update_user(id, user_update)
#         return updated_user
#     except Exception as e:
#         raise Exception(f"Unable to update the user due to the following error: {e}")
    
# @router.delete("/{id}")
# async def delete_user(id: UUID):
#     try:
#         deleted_user = await crud.delete_user(id)
#         return deleted_user.deleted_count
#     except Exception as e:
#         raise Exception(f"Unable to delete the user due to the following error: {e}")
    

