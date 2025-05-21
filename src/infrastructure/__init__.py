"""Shared infrastructure components.

This module exposes a very small persistence wrapper.  It attempts to use
``sqlalchemy`` when available but falls back to Python's built in ``sqlite3``
module so the code base can run in extremely constrained offline
environments.  Only a single SQLite database file is supported which lives in
the project directory.
"""

from __future__ import annotations

import importlib.util
import sqlite3
from pathlib import Path
from typing import Any


DB_PATH = Path(__file__).resolve().parent / "app.db"

_SQLALCHEMY_AVAILABLE = importlib.util.find_spec("sqlalchemy") is not None

if _SQLALCHEMY_AVAILABLE:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker

    _engine = create_engine(
        f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False}
    )
    _Session = sessionmaker(bind=_engine)

    def get_session() -> Session:
        """Return a SQLAlchemy :class:`~sqlalchemy.orm.Session`."""

        return _Session()

    def get_connection() -> sqlite3.Connection:
        """Return a raw DB-API connection."""

        return _engine.raw_connection()
else:

    def get_connection() -> sqlite3.Connection:
        """Return a plain :class:`sqlite3.Connection`."""

        return sqlite3.connect(DB_PATH)

    def get_session() -> sqlite3.Connection:
        """Alias for :func:`get_connection` when SQLAlchemy is unavailable."""

        return get_connection()


def init_db() -> None:
    """Initialise the local database with minimal schema."""

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


__all__ = [
    "get_session",
    "get_connection",
    "init_db",
]

