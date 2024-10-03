from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.domain.models import Base
from migrations.database import engine
from routes.api.v1 import (
    auth_routes,
    user_routes
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    lifespan=lifespan,
    title="FastAPI Supercharged",
    description="FastAPI Supercharged is a FastAPI project template with some superpowers.",
    version="1.0.0"
)

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
