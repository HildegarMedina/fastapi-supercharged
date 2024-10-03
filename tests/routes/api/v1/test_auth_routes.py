"""Routes Auth test file."""
import pytest
from tests.fixtures.user import create_user

HEADERS = {
    "Content-Type": "application/json"
}

@pytest.mark.asyncio
async def test_authenticate(setup):
    """Test the api/v1/auth post route."""
    repo, client = setup
    await create_user(repo)
    payload = {
        "username": "john.doe@gmail.com",
        "password": "password"
    }
    response = client.post("/api/v1/auth", data=payload)
    assert response.status_code == 200
    assert response.json()["access_token"]

@pytest.mark.asyncio
async def test_me(setup, login_user):
    """Test the api/v1/auth/me get route."""
    _, client = setup
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {login_user}"
    response = client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1
