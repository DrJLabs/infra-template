"""Authentication API router."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login() -> dict[str, str]:
    """Return a dummy authentication token."""
    return {"token": "dummy-token"}
