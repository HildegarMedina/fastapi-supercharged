from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.domain.models import Base
from migrations.database import engine
from routes.api.v1 import user_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router)
