"""Application entrypoint wiring infrastructure and feature slices."""

from fastapi import FastAPI
from src.features.auth.api import router as auth_router
from src.features.orders.api import router as orders_router

app = FastAPI()

# Mount feature routers. Actual implementations live in each feature slice.
app.include_router(auth_router, prefix="/auth")
app.include_router(orders_router, prefix="/orders")

__all__ = ["app"]
