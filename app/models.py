from pydantic import Field
from beanie import Document


class UsersModel(Document):
    name: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    email: str = Field(...)