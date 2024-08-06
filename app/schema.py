from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr = Field(max_length=255)
    full_name: str | None = Field(default=None, max_length=255)
    age: int | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)

class UserIn(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserOut(UserBase):
    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str

class UserUpdateBase(BaseModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)
    age: int | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None, max_length=255)

class UserUpdateIn(UserUpdateBase):
    password: str | None = Field(default=None, min_length=8, max_length=40)

class UserUpdateInDB(UserUpdateBase):
    hashed_password: str | None = Field(default=None)

class UserLogin(BaseModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)