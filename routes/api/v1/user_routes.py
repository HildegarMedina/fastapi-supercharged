from typing import List

from fastapi import APIRouter

from app.controllers.user_controller import UserController
from app.schemas.requests.user_requests import CreateUserRequest
from app.schemas.responses.user_responses import CreateUserResponse, UserResponse
from app.services.user_service import UserService
from migrations.database import AsyncSessionLocal


router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)

repo = AsyncSessionLocal()
user_service = UserService(repo)
user_controller = UserController(user_service)


@router.get('', response_model=List[UserResponse])
async def get_list_users():
    return await user_controller.get_list_users()


@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    return await user_controller.get_user(user_id)


@router.post('', status_code=201, response_model=CreateUserResponse)
async def create_user(data: CreateUserRequest):
    return await user_controller.create_user(data)


@router.put('/{user_id}', status_code=204)
async def update_user(user_id: int, data: CreateUserRequest):
    return await user_controller.update_user(user_id, data)


@router.delete('/{user_id}', status_code=204)
async def delete_user(user_id: int):
    return await user_controller.delete_user(user_id)
