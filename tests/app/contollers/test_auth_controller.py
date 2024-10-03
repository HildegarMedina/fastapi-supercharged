import pytest
from fastapi import HTTPException
from fixtures.user import create_user, delete_user
from app.schemas.requests.auth_requests import CredentialsRequest

CREDENTIALS = CredentialsRequest(
    username="john.doe@gmail.com",
    password="password"
)

@pytest.mark.asyncio
async def test_login(setup, auth_controller):
    repo, _ = setup
    await create_user(repo)
    response = await auth_controller.login(CREDENTIALS)
    assert response["access_token"]

@pytest.mark.asyncio
async def test_login_failed(auth_controller):
    with pytest.raises(HTTPException) as exc:
        await auth_controller.login(CREDENTIALS)
    assert exc.value.status_code == 401
    assert exc.value.detail == "Invalid Credentials"

@pytest.mark.asyncio
async def test_get_logged_user(auth_controller, login_user):
    response = await auth_controller.get_logged_user(login_user)
    assert response

@pytest.mark.asyncio
async def test_get_logged_user_invalid_token(auth_controller):
    with pytest.raises(HTTPException) as exc:
        await auth_controller.get_logged_user("invalid_token")
    assert exc.value.status_code == 401
    assert exc.value.detail == "Could not validate credentials"

@pytest.mark.asyncio
async def test_get_logged_user_not_found(setup, auth_controller, login_user):
    repo, _ = setup
    with pytest.raises(HTTPException) as exc:
        await delete_user(repo, 1)
        await auth_controller.get_logged_user(login_user)
    assert exc.value.status_code == 401
    assert exc.value.detail == "Could not validate credentials"
