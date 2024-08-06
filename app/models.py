from pydantic import Field, EmailStr
from beanie import Document, Indexed
from uuid import UUID, uuid4
from typing import Annotated


# Database model for users
class User(Document):
    id: UUID = Field(default_factory=uuid4)
    email: Annotated[EmailStr, Indexed(unique=True)]
    hashed_password: str = Field(...)
    username: str | None = Field(...)
    age: int | None = Field(...)
    gender: str | None = Field(...)

    class Settings:
        name = "users"

# JSON payload containing access token
class Token(Document):
    access_token: str = Field(...)
    token_type: str = "bearer"

    class Settings:
        name = "tokens"