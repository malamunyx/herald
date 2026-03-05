from typing import Generator

from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.database_url)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
