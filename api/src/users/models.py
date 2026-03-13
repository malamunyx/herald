from uuid import UUID, uuid7

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    bio: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
