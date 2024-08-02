from pydantic import BaseModel, Field, EmailStr

class UserIn(BaseModel):
    username: str = Field(title="Name of the user", max_length=300)
    email: EmailStr
    password: str
    age: int | None = Field(default=None, gt=0, description="The age must be greater than zero")
    gender: str | None = None


class UserOut(BaseModel):
    username: str = Field(title="Name of the user", max_length=300)
    email: EmailStr | None = None
    age: int | None = Field(default=None, gt=0, description="The age must be greater than zero")
    gender: str | None = None

    class Config:
        orm_mode = True