from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
