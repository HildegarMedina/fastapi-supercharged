import pytest
from tests.fixtures.user import create_user
from app.schemas.requests.user_requests import CreateUserRequest
import jwt
from datetime import datetime, timedelta, timezone
from config.config import SECRET_KEY, ALGORITHM
from tests.mocks.user import USER_MOCK

@pytest.mark.asyncio
async def test_login(setup, auth_svc, user_svc):
    """Test login success."""
    repo, _ = setup
    await create_user(repo)
    response = await auth_svc.login(user_svc, "john.doe@gmail.com", "password")
    assert response["access_token"]


@pytest.mark.asyncio
async def test_login_failed(auth_svc, user_svc):
    """Test login failed."""
    response = await auth_svc.login(user_svc, "john.doe@gmail.com", "password")
    assert response is False

@pytest.mark.asyncio
def test_create_access_token(auth_svc):
    """Test create_access_token generates a valid JWT."""
    user = CreateUserRequest(**USER_MOCK)
    iat = datetime.now(timezone.utc)
    expire = iat + timedelta(minutes=15)
    token = auth_svc.create_access_token(user, iat, expire)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_token["sub"] == user.email
    assert decoded_token["iat"] == int(iat.timestamp())
    assert decoded_token["exp"] == int(expire.timestamp())
