from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer

from app.controllers.auth_controller import AuthController
from app.domain.models import User
from app.schemas.requests.auth_requests import CredentialsRequest
from app.schemas.responses.auth_responses import SuccessLoginResponse, UserLoggedResponse
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from migrations.database import AsyncSessionLocal


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)

repo = AsyncSessionLocal()
auth_service = AuthService(repo)
user_service = UserService(repo)
user_controller = AuthController(auth_service, user_service)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth")


@router.post('', status_code=200, response_model=SuccessLoginResponse)
async def authenticate(
    username: str = Form(),
    password: str = Form(),
):
    data = CredentialsRequest(username=username, password=password)
    return await user_controller.login(data)


@router.get('/me', status_code=200, response_model=UserLoggedResponse)
async def get_logged_user(
    logged_user: Annotated[User, Depends(user_controller.get_logged_user)]
):
    return logged_user
