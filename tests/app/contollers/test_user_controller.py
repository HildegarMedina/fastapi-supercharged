import pytest
from app.schemas.requests.user_requests import CreateUserRequest
from fastapi import HTTPException
from fixtures.user import create_user
from tests.mocks.user import USER_MOCK

@pytest.mark.asyncio
async def test_get_user_found(setup, user_controller):
    repo, _ = setup
    user_saved = await create_user(repo)
    response = await user_controller.get_user(1)
    assert response.id == user_saved.id

@pytest.mark.asyncio
async def test_get_user_not_found(user_controller):
    with pytest.raises(HTTPException) as exc:
        await user_controller.get_user(1)
    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found."

@pytest.mark.asyncio
async def test_get_list_users(user_controller, setup):
    repo, _ = setup
    await create_user(repo)
    response = await user_controller.get_list_users()
    assert len(response) == 1

@pytest.mark.asyncio
async def test_create_user_success(user_controller):
    user_mock = CreateUserRequest(**USER_MOCK)
    response = await user_controller.create_user(user_mock)
    assert response.id

@pytest.mark.asyncio
async def test_create_user_integrity_error(user_controller, setup):
    repo, _ = setup
    await create_user(repo, email="john.doe@gmail.com")
    with pytest.raises(HTTPException) as exc:
        user_mock = CreateUserRequest(**USER_MOCK)
        await user_controller.create_user(user_mock)
    assert exc.value.status_code == 400
    assert exc.value.detail == "Email already exists."

@pytest.mark.asyncio
async def test_update_user_success(user_controller, setup):
    repo, _ = setup
    user_saved = await create_user(repo)
    user_mock = CreateUserRequest(**USER_MOCK)
    user_mock.first_name = "Changed"
    response = await user_controller.update_user(user_saved.id, user_mock)
    assert response is None

@pytest.mark.asyncio
async def test_update_user_integrity_error(user_controller, setup):
    repo, _ = setup
    email_already_exists = "john@gmail.com"
    await create_user(repo, email=email_already_exists)
    user_saved = await create_user(repo)
    user_mock = CreateUserRequest(**USER_MOCK)
    user_mock.email = email_already_exists
    with pytest.raises(HTTPException) as exc:
        await user_controller.update_user(user_saved.id, user_mock)
    assert exc.value.status_code == 400
    assert exc.value.detail == "Email already exists."

@pytest.mark.asyncio
async def test_delete_user_found(user_controller, setup):
    repo, _ = setup
    user_saved = await create_user(repo)
    response = await user_controller.delete_user(user_saved.id)
    assert response is None

@pytest.mark.asyncio
async def test_delete_user_not_found(user_controller):
    with pytest.raises(HTTPException) as exc:
        await user_controller.delete_user(1234)
    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found."
