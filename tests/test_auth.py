import pytest
from fastapi import HTTPException

from src.features.auth.api import login, LoginRequest


def test_login_success():
    payload = LoginRequest(username="admin", password="secret")
    assert login(payload) == {"token": "fake-token"}


def test_login_failure():
    payload = LoginRequest(username="user", password="bad")
    with pytest.raises(HTTPException):
        login(payload)
