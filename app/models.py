from pydantic import Field
from beanie import Document
from uuid import UUID, uuid4



# Database model for users
class User(Document):
    id: UUID = Field(default_factory=uuid4)
    username: str = Field(...)
    email: str = Field(...)
    hashed_password: str = Field(...)
    age: int | None = Field(...)
    gender: str | None = Field(...)

    class Settings:
        name = "users"

# JSON payload containing access token
class Token(Document):
    access_token: str = Field(...)
    token_type: str = "bearer"