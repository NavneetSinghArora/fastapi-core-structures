"""This module contains base models for the application."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, Session, DeclarativeBase, sessionmaker, mapped_column

from constants import SQLITE_DATABASE_URL


class Base(DeclarativeBase):
    """This is the base class for all models."""

    pass


class Users(Base):
    """This is the Users model."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)


class SQLiteSession:
    """This is the SQLite session class."""

    def __init__(self) -> None:
        """This is the constructor."""
        self._engine = create_engine(SQLITE_DATABASE_URL)
        Base.metadata.create_all(bind=self._engine)
        self._SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=self._engine)

    def get_session(self) -> Session:
        """This is the get session method."""
        return self._SessionLocal()
