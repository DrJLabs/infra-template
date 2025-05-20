import pytest
from fastapi import HTTPException

from src.features.orders.api import list_orders, get_order, orders_db


def test_list_orders():
    result = list_orders()
    assert len(result) == len(orders_db)


def test_get_order_success():
    result = get_order(1)
    assert result.id == 1


def test_get_order_not_found():
    with pytest.raises(HTTPException):
        get_order(999)
