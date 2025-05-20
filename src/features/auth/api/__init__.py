"""Authentication API endpoints."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()


class LoginRequest(BaseModel):
    """Simple login payload."""

    username: str
    password: str


@router.post("/login")
def login(payload: LoginRequest) -> dict:
    """Authenticate a user and return a fake token."""

    if payload.username == "admin" and payload.password == "secret":
        return {"token": "fake-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


__all__ = ["router", "login", "LoginRequest"]
