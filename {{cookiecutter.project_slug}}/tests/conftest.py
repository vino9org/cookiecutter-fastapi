import asyncio
import os
import sys

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

os.environ["ENV"] = "TEST"
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(f"{cwd}/.."))

from {{ cookiecutter.pkg_name }} import app  # noqa: E402


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://localhost:8080") as client, LifespanManager(app):
        yield client
