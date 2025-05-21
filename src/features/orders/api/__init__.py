"""Order API endpoints using the shared persistence layer."""

from fastapi import APIRouter, Depends

from src.infrastructure import get_connection, init_db


router = APIRouter()


@router.on_event("startup")
def _startup() -> None:
    """Ensure the database schema exists."""

    init_db()


def _db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()


@router.post("/")
def create_order(item: str, conn=Depends(_db)) -> dict:
    """Persist a new order item."""

    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (item) VALUES (?)", (item,))
    conn.commit()
    return {"id": cursor.lastrowid, "item": item}


@router.get("/")
def list_orders(conn=Depends(_db)) -> list[dict]:
    """Return all persisted orders."""

    cursor = conn.cursor()
    rows = cursor.execute("SELECT id, item FROM orders").fetchall()
    return [{"id": row[0], "item": row[1]} for row in rows]
