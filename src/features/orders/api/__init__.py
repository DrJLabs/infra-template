"""Orders API endpoints."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()


class Order(BaseModel):
    id: int
    item: str


orders_db = [
    Order(id=1, item="apple"),
    Order(id=2, item="orange"),
]


@router.get("/")
def list_orders() -> list[Order]:
    """Return all orders."""

    return orders_db


@router.get("/{order_id}")
def get_order(order_id: int) -> Order:
    """Return a single order by ID."""

    for order in orders_db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


__all__ = ["router", "list_orders", "get_order", "orders_db", "Order"]
