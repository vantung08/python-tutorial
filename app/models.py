from pydantic import Field
from beanie import Document


class User(Document):
    username: str = Field(...)
    email: str = Field(...)
    hashed_password: str = Field(...)
    age: int | None = Field(...)
    gender: str | None = Field(...)

    class Settings:
        name = "users"