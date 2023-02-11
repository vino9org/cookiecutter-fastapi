from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel import Session

from {{ cookiecutter.pkg_name }}.database import get_session
from {{ cookiecutter.pkg_name }}.models import User, UserRecord

app = FastAPI()


@app.get("/healthz", include_in_schema=False)
async def health():
    return "running"


@app.get("/ready", include_in_schema=False)
async def ready():
    return "ready"


@app.get("/users", response_model=list[User])
async def get_users(session: Session = Depends(get_session)) -> List[User]:
    result = await session.execute(select(UserRecord))  # type: ignore # Incompatible types
    records = result.scalars().all()
    return [User(user_name=rec.user_name, comments=rec.comments) for rec in records]
