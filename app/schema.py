from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    username: str = Field(title="Name of the user", max_length=300)
    email: EmailStr | None = None
    age: int | None = Field(default=None, gt=0, description="The age must be greater than zero")
    gender: str | None = None

class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    class Config:
        orm_mode = True