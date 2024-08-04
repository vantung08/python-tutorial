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

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    age: int | None = None
    gender: str | None = None
    password: str | None = None

class UserUpdateInDB(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    age: int | None = None
    gender: str | None = None
    hashed_password: str | None = None

class UserInDB(UserBase):
    hashed_password: str