from pydantic import Field
from beanie import Document


class Users(Document):
    name: str = Field(...)
    age: int = Field(...)
    gender: str | None = Field(...)
    email: str | None = Field(...)

    class Settings:
        name = "users"