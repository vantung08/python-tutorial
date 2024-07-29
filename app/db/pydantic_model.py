from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(title="Name of the user", max_length=300)
    age: int = Field(default=None, gt=0, description="The price must be greater than zero")
    gender: str = None
    email: str | None = None