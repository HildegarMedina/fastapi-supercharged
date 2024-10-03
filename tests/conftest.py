import pytest_asyncio
from fastapi.testclient import TestClient
from main import app
from migrations.database import AsyncSessionLocal, engine
from app.domain.models import Base
import asyncio
import pytest
from sqlalchemy import text

# Importing Services and Controllers
from fixtures.user import user_svc, user_controller
from fixtures.auth import login_user, auth_svc, auth_controller

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="function")
async def setup():
    async with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            await conn.execute(text(f"DELETE FROM {table.name}"))

    repository = AsyncSessionLocal()
    with TestClient(app) as client:
        yield repository, client 

    await repository.close()
