from fastapi import APIRouter

from backend.app.api.v1.endpoints import auth, widgets, todos

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(widgets.router, prefix="/widgets", tags=["widgets"])
api_router.include_router(todos.router, prefix="/todos", tags=["todos"])
