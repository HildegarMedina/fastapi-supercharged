from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL, SHOW_LOG_DATABASE
from app.repository.repository import Repository
import os

db_url = DATABASE_URL
if os.environ.get("RUNNING_TESTS"):
    db_url = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(db_url, echo=SHOW_LOG_DATABASE)

AsyncSessionLocal = sessionmaker(bind=engine, class_=Repository, expire_on_commit=False)
