from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.db.base import get_db

router = APIRouter()


@router.post("/login")
async def login(db: AsyncSession = Depends(get_db)):
    # TODO: 实现登录逻辑
    return {"msg": "Login endpoint"}


@router.post("/register")
async def register(db: AsyncSession = Depends(get_db)):
    # TODO: 实现注册逻辑
    return {"msg": "Register endpoint"}
