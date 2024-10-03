from pydantic import BaseModel

from app.schemas.generics import TimeStamp


class SuccessLoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserLoggedResponse(BaseModel, TimeStamp):
    id: int
    email: str
    first_name: str
    last_name: str
