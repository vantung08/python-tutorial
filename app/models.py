from pydantic import BaseModel, Field


class UsersModel(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    email: str = Field(...)