"""Configurations for the application."""
DATABASE_URL = "postgresql+psycopg://postgres:123123@localhost:5432/fastapi_supercharged"
SHOW_LOG_DATABASE = False
SECRET_KEY = "0bb837ab4eb109c150c28c477860bd5a0d672c05f6ad1470c09c54438cdf649f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
