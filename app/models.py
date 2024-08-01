from pydantic import Field
from beanie import Document


class User(Document):
    name: str = Field(...)
    age: int | None = Field(...)
    gender: str | None = Field(...)
    email: str | None = Field(...)

    class Settings:
        name = "users"