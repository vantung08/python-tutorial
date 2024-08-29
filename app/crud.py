from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User
from app.schema import UserCreate, UserInDB, UserUpdate, UserUpdateInDB, Message
from app.core.security import get_password_hash, verify_password
from fastapi import HTTPException, status
from pydantic import EmailStr
from uuid import UUID

def create_user(*, session: Session, schema_user: UserCreate) -> User:
    hashed_password = get_password_hash(schema_user.password)
    In_DB_user = UserInDB(**schema_user.model_dump(), hashed_password=hashed_password)
    db_obj = User(**In_DB_user.model_dump())
    session.add(db_obj)
    session.flush()
    session.refresh(db_obj)
    return db_obj

def get_user_by_email(*, session: Session, email: EmailStr) -> User | None:
    stm = select(User).where(User.email == email)
    user = session.scalars(stm).first()
    return user

def get_user_by_id(*, session: Session, id: UUID) -> User | None:
    stm = select(User).where(User.id == id)
    user = session.scalars(stm).first()
    return user

def get_all_user(*, session: Session) -> list[User]:
    stm = select(User)
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
    user = session.scalars(select(User).where(User.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="User record not found!")
    for key, value in filter_user_update.items():
        if hasattr(user, key):
            setattr(user, key, value)
    updated_user = session.scalars(select(User).where(User.id == id)).first()
    session.flush()
    session.refresh(updated_user)
    return updated_user

def delete_user(*, session: Session, id: UUID):
    user = session.scalars(select(User).where(User.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User record not found!")
    session.delete(user)
    return Message(message="User deleted successfully")

def authenticate_user(*, session: Session, email: str, password: str) -> User:
    user = get_user_by_email(session=session, email=email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User record by email not found")
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    return user


# from app.models import User
# from app.schema import UserIn, UserInDB, UserUpdateIn, UserUpdateInDB
# from app.core.security import get_password_hash
# from fastapi import HTTPException
# from pydantic import EmailStr
# from app.core.security import verify_password
# from uuid import UUID

# async def create_user(schema_user: UserIn):
#     hashed_password = get_password_hash(schema_user.password)
#     In_DB_user = UserInDB(**schema_user.model_dump(), hashed_password=hashed_password)
#     model_user = User(**In_DB_user.model_dump())
#     new_user = await User.insert_one(model_user)
#     return new_user

# async def get_user_by_email(email: EmailStr) -> User:
#     user = await User.find_one(User.email == email)
#     if not user:
#         raise HTTPException(status_code=404, detail="User record not found!")
#     return user

# async def get_user_by_id(id: UUID) -> User:
#     user = await User.get(id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User record not found!")
#     return user

# async def get_all_user() -> list[User]:
#     users = await User.find().to_list()
#     if not users:
#         raise HTTPException(status_code=404, detail="User record not found!")
#     return users

# async def update_user(id: UUID, user_update: UserUpdateIn):
#     if user_update.password is not None:
#         hashed_password = get_password_hash(user_update.password)
#         user_update = UserUpdateInDB(**user_update.model_dump(), hashed_password=hashed_password)
#     filter_user_update = {k: v for k, v in user_update.model_dump().items() if v is not None}
#     update_query = {"$set": {
#         field: value for field, value in filter_user_update.items()
#     }}
#     user = await User.get(id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User record not found!")
#     updated_user = await user.update(update_query)
#     updated_user = await User.get(id)
#     return updated_user

# async def delete_user(id: UUID):
#     user = await User.get(id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User record not found!")
#     delete_user = await user.delete()
#     return delete_user

# async def authenticate_user(email: str, password: str) -> User:
#     user = await get_user_by_email(email)
#     if not user:
#         raise HTTPException(status_code=404, detail="User record by email not found")
#     if not verify_password(password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
#     return user