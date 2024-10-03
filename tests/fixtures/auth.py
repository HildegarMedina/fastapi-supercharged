import pytest
import pytest_asyncio
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.controllers.auth_controller import AuthController
from tests.fixtures.user import create_user


@pytest.fixture
def auth_svc(setup):
    repo, _ = setup
    return AuthService(repo)

@pytest.fixture
def auth_controller(auth_svc):
    user_service = UserService(auth_svc.repo)
    return AuthController(auth_svc, user_service)

@pytest_asyncio.fixture
async def login_user(setup, auth_svc, user_svc):
    repo, _ = setup
    await create_user(repo)
    email = "john.doe@gmail.com"
    password = "password"
    login_response = await auth_svc.login(user_svc, email, password)
    return login_response['access_token']
