import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    ECHO_SQL: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    if os.environ.get("ENV") != "TEST":
        return Settings()
    else:
        # use in memory sqlite for testing
        return Settings(SQLALCHEMY_DATABASE_URL="sqlite+aiosqlite://")
