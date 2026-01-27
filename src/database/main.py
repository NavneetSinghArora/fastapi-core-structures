"""This module contains database connection logic."""

from collections.abc import Generator

from database.models import SQLiteSession


def get_database_connection() -> Generator:
    """This is a context manager that provides a database connection."""
    connection = SQLiteSession().get_session()
    try:
        yield connection
    except Exception:
        raise Exception("Failed to get database connection")
    finally:
        connection.close()
