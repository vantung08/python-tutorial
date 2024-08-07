from pydantic import Field, EmailStr
from beanie import Document, Indexed
from uuid import UUID, uuid4
from typing import Annotated


# Database model for users
class User(Document):
    id: UUID = Field(default_factory=uuid4)
    email: Annotated[EmailStr, Indexed(unique=True)] = Field(max_length=255)
    hashed_password: str = Field(...)
    is_active: bool = True
    full_name: str | None = Field(default=None, max_length=255)
    age: int | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)

    class Settings:
        name = "users"

# JSON payload containing access token
# class Token(Document):
#     access_token: str = Field(...)
#     token_type: str = "bearer"

#     class Settings:
#         name = "tokens"

# # Content of JWT token
# class TokenPayload(Document):
#     sub: str | None = None