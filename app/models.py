from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import Optional

from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    full_name = Column(String, nullable=True, default=None)
    age = Column(Integer, nullable=True, default=None)
    gender = Column(String, nullable=True, default=None)








#-------------------------------------
# from pydantic import Field, EmailStr
# from beanie import Document, Indexed
# from uuid import UUID, uuid4
# from typing import Annotated


# # Database model for users
# class User(Document):
#     id: UUID = Field(default_factory=uuid4)
#     email: Annotated[EmailStr, Indexed(unique=True)] = Field(max_length=255)
#     hashed_password: str = Field(...)
#     is_active: bool = True
#     full_name: str | None = Field(default=None, max_length=255)
#     age: int | None = Field(default=None, max_length=255)
#     gender: str | None = Field(default=None, max_length=255)

#     class Settings:
#         name = "users"
