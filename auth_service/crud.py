from sqlalchemy.orm import Session
from sqlalchemy import select
from auth_service.models import AuthUser
from auth_service.schema import UserCreate, UserInDB, UserUpdate, UserUpdateInDB, Message
from auth_service.core.security import get_password_hash, verify_password
from fastapi import HTTPException, status
from pydantic import EmailStr
from uuid import UUID

def create_user(*, session: Session, schema_user: UserCreate) -> AuthUser:
    hashed_password = get_password_hash(schema_user.password)
    In_DB_user = UserInDB(**schema_user.model_dump(), hashed_password=hashed_password)
    db_obj = AuthUser(**In_DB_user.model_dump())
    session.add(db_obj)
    session.flush()
    session.refresh(db_obj)
    return db_obj

def get_user_by_email(*, session: Session, email: EmailStr) -> AuthUser | None:
    stm = select(AuthUser).where(AuthUser.email == email)
    user = session.scalars(stm).first()
    return user

def get_user_by_id(*, session: Session, id: UUID) -> AuthUser | None:
    stm = select(AuthUser).where(AuthUser.id == id)
    user = session.scalars(stm).first()
    return user

def get_all_user(*, session: Session) -> list[AuthUser]:
    stm = select(AuthUser)
    users = session.scalars(stm)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="User record not found!")
    return users

def update_user(*, session: Session, id: UUID, user_update: UserUpdate):
    if user_update.password is not None:
        hashed_password = get_password_hash(user_update.password)
        user_update = UserUpdateInDB(**user_update.model_dump(), hashed_password=hashed_password)
    filter_user_update = {k: v for k, v in user_update.model_dump().items() if v is not None}
    user = session.scalars(select(AuthUser).where(AuthUser.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="User record not found!")
    for key, value in filter_user_update.items():
        if hasattr(user, key):
            setattr(user, key, value)
    updated_user = session.scalars(select(AuthUser).where(AuthUser.id == id)).first()
    session.flush()
    session.refresh(updated_user)
    return updated_user

def delete_user(*, session: Session, id: UUID):
    user = session.scalars(select(AuthUser).where(AuthUser.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User record not found!")
    session.delete(user)
    return Message(message="User deleted successfully")

def authenticate_user(*, session: Session, email: str, password: str) -> AuthUser:
    user = get_user_by_email(session=session, email=email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User record by email not found")
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    return user