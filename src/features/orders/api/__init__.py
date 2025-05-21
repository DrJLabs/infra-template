"""Order API endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel

from typing import List


router = APIRouter()


class OrderCreate(BaseModel):
    """Payload required to create an order."""

    item: str
    quantity: int


class Order(OrderCreate):
    """Order representation returned to clients."""

    id: int


_orders: List[Order] = []
_next_id = 1


@router.get("/", response_model=List[Order])
def list_orders() -> List[Order]:
    """Return all created orders."""

    return _orders


@router.post("/", response_model=Order, status_code=201)
def create_order(payload: OrderCreate) -> Order:
    """Create a new order and return it."""

    global _next_id
    order = Order(id=_next_id, **payload.dict())
    _next_id += 1
    _orders.append(order)
    return order
