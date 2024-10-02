import pytest_asyncio
from fastapi.testclient import TestClient
from main import app
from migrations.database import AsyncSessionLocal, engine
from app.domain.models import Base
import asyncio
import pytest

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="function")
async def setup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    repository = AsyncSessionLocal()
    with TestClient(app) as client:
        yield repository, client 

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await repository.close()
