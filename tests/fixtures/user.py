from app.schemas.requests.user_requests import CreateUserRequest
from app.services.user_service import UserService
import pytest
from app.controllers.user_controller import UserController

@pytest.fixture
def user_svc(setup):
    repo, _ = setup
    return UserService(repo)

@pytest.fixture
def user_controller(user_svc):
    return UserController(user_svc)

async def create_user(repo, first_name="John", last_name="Doe", email="john.doe@gmail.com", password="password"):
    user_svc = UserService(repo)
    user_object = CreateUserRequest(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    ) 
    return await user_svc.create(user_object)

async def delete_user(repo, user_id):
    user_svc = UserService(repo)
    user = await user_svc.get(user_id)
    await user_svc.delete(user)
