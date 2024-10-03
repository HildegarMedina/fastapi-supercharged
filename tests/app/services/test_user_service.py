import pytest
from tests.fixtures.user import create_user
from app.schemas.requests.user_requests import CreateUserRequest
from tests.mocks.user import USER_MOCK

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
    payload = CreateUserRequest(**USER_MOCK)
    user = await user_svc.create(payload)
    assert user.id is not None

@pytest.mark.asyncio
async def test_update(setup, user_svc):
    """Test update user."""
    repo, _ = setup
    user = await create_user(repo)
    payload = CreateUserRequest(**USER_MOCK)
    payload.password = None
    await user_svc.update(user.id, payload)
    found = await user_svc.get(user.id)
    assert found.first_name == USER_MOCK["first_name"]

@pytest.mark.asyncio
async def test_delete(setup, user_svc):
    """Test delete user."""
    repo, _ = setup
    user = await create_user(repo)
    found = await user_svc.get(user.id)
    await user_svc.delete(found)
    found = await user_svc.get(user.id)
    assert found is None
