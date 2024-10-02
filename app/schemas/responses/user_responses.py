from datetime import datetime
from typing import Union

from pydantic import BaseModel


class TimeStampResponse(BaseModel):
    created_at: datetime
    modified_at: datetime
    created_by: Union[int, None]
    modified_by: Union[int, None]


class UserResponse(TimeStampResponse):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        """Config for UserResponse."""

        orm_mode = True


class CreateUserResponse(BaseModel):
    id: int
