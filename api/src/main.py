from fastapi import FastAPI

from src.config import settings
from src.users.router import users_router

app = FastAPI()

app.include_router(users_router, prefix=settings.api_prefix)
