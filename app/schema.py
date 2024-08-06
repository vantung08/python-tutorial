from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str | None = None
    age: int | None = None
    gender: str | None = None

class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str

class UserUpdateBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    age: int | None = None
    gender: str | None = None

class UserUpdateIn(UserUpdateBase):
    password: str | None = None

class UserUpdateInDB(UserUpdateBase):
    hashed_password: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str