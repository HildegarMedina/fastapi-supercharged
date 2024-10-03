from pydantic import BaseModel

from app.schemas.generics import TimeStamp


class UserResponse(BaseModel, TimeStamp):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        """Config for UserResponse."""

        orm_mode = True


class CreateUserResponse(BaseModel):
    id: int
