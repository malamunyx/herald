from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.users.schema import UserResponse

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/{user_id}", response_model=UserResponse)
def get_user(db: Annotated[Session, Depends(get_db)], user_id: UUID):
    raise NotImplementedError
