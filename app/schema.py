from pydantic import BaseModel, EmailStr, Field
import uuid

class UserBase(BaseModel):
    email: EmailStr = Field(max_length=255)
    full_name: str | None = Field(default=None, max_length=255)
    is_active: bool = Field(default=True)
    age: int | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserPublish(UserBase):
    id: uuid.UUID
    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)
    password: str | None = Field(default=None, min_length=8, max_length=40)

class UserUpdateInDB(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)
    hashed_password: str | None = Field(default=None)

class UserLogin(BaseModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)

class Token(BaseModel):
    access_token: str = Field(...)
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: str | None = None

class Message(BaseModel):
    message: str