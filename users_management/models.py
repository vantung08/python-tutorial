from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from uuid import UUID

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[UUID] = mapped_column(ForeignKey("auth_users.id", ondelete="CASCADE"), primary_key=True)
    full_name: Mapped[str | None] = mapped_column(default=None)
    age: Mapped[int | None] = mapped_column(default=None)
    gender: Mapped[str | None] = mapped_column(default=None)
    # email: Mapped[str] = mapped_column(unique=True, index=True)
    # hashed_password: Mapped[str] = mapped_column()
    # is_active: Mapped[bool] = mapped_column(default=True)








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
