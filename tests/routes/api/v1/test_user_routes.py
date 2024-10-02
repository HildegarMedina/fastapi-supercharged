"""Routes User test file."""
import pytest
from tests.fixtures.user import create_user

HEADERS = {
    "Content-Type": "application/json"
}

PAYLOAD_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@gmail.com",
    "password": "password"
}

@pytest.mark.asyncio
async def test_get_list_users(setup):
    """Test the api/v1/users get route."""
    repo, client = setup
    await create_user(repo)
    response = client.get("/api/v1/users", headers=HEADERS)
    assert response.status_code == 200
    assert len(response.json()) == 1 

@pytest.mark.asyncio
async def test_get_user(setup):
    """Test the ap1/v1/users/{user_id} get route."""
    repo, client = setup
    user = await create_user(repo)
    response = client.get(f"/api/v1/users/{user.id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == user.id

@pytest.mark.asyncio
async def test_get_user(setup):
    """Test the ap1/v1/users/{user_id} get route."""
    repo, client = setup
    user = await create_user(repo)
    response = client.get(f"/api/v1/users/{user.id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == user.id

@pytest.mark.asyncio
async def test_create_user(setup):
    """Test the api/v1/users post route."""
    _, client = setup
    response = client.post("/api/v1/users", headers=HEADERS, json=PAYLOAD_USER)
    assert response.status_code == 201
    assert response.json()["id"]

@pytest.mark.asyncio
async def test_update_user(setup):
    """Test the api/v1/users put route."""
    repo, client = setup
    user = await create_user(repo)
    response = client.put(f"/api/v1/users/{user.id}", headers=HEADERS, json=PAYLOAD_USER)
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_delete_user(setup):
    """Test the api/v1/users delete route."""
    repo, client = setup
    user = await create_user(repo)
    response = client.delete(f"/api/v1/users/{user.id}", headers=HEADERS)
    assert response.status_code == 204
    response = client.get(f"/api/v1/users/{user.id}", headers=HEADERS)
    assert response.status_code == 404
