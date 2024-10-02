import pytest
from tests.fixtures.user import create_user
from app.schemas.requests.user_requests import CreateUserRequest
from tests.fixtures.user import user_svc

PAYLOAD_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@gmail.com",
    "password": "password"
}

@pytest.mark.asyncio
async def test_get(setup, user_svc):
    """Test get user."""
    repo, _ = setup
    user = await create_user(repo)
    found = await user_svc.get(user.id)
    assert found.id == user.id

@pytest.mark.asyncio
async def test_get_list(setup, user_svc):
    """Test get list user."""
    repo, _ = setup
    total_user = 3
    for n in range(total_user):
        await create_user(repo, email=f"email{n}@gmail.com")
    list = await user_svc.get_list()
    assert len(list) == total_user

@pytest.mark.asyncio
async def test_create(user_svc):
    """Test create user."""
    payload = CreateUserRequest(**PAYLOAD_USER)
    user = await user_svc.create(payload)
    assert user.id is not None

@pytest.mark.asyncio
async def test_update(setup, user_svc):
    """Test update user."""
    repo, _ = setup
    user = await create_user(repo)
    payload = CreateUserRequest(**PAYLOAD_USER)
    payload.password = None
    await user_svc.update(user.id, payload)
    found = await user_svc.get(user.id)
    assert found.first_name == PAYLOAD_USER["first_name"]

@pytest.mark.asyncio
async def test_delete(setup, user_svc):
    """Test delete user."""
    repo, _ = setup
    user = await create_user(repo)
    found = await user_svc.get(user.id)
    await user_svc.delete(found)
    found = await user_svc.get(user.id)
    assert found is None
