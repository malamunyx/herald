from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.users.models import User


def get_user(db: Session, user_id: UUID) -> User | None:
    stmt = select(User).where(User.id == user_id)
    return db.scalars(stmt).first()


def update_user(db: Session, user_id: UUID) -> User | None:
    raise NotImplementedError


def delete_user(db: Session, user_id: UUID) -> User | None:
    user = get_user(db, user_id)
    if not user:
        return None
    user.is_active = False
    db.commit()
    return user
