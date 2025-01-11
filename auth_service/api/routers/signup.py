from fastapi import APIRouter, HTTPException, status
from auth_service import crud
from auth_service.schema import UserCreate, UserPublish
from auth_service.api.deps import SessionDep
from typing import Any

router = APIRouter(
    prefix="/signup"
    )

    
@router.post("/", response_model=UserPublish)
def register_user(user_create: UserCreate, session: SessionDep) -> Any:
    user = crud.get_user_by_email(session=session, email=user_create.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="The user with this email already exists in the system.")
    registered_user = crud.create_user(session=session, schema_user=user_create)
    return registered_user