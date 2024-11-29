from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.db.base import get_db
from backend.app.models.widget import Widget
from backend.app.schemas.widget import WidgetCreate, WidgetUpdate, Widget as WidgetSchema

router = APIRouter()

@router.get("/", response_model=List[WidgetSchema])
async def get_widgets(
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    result = await db.execute(select(Widget))
    widgets = result.scalars().all()
    return widgets

@router.post("/", response_model=WidgetSchema)
async def create_widget(
    widget: WidgetCreate,
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    db_widget = Widget(
        # user_id=current_user.id,  # TODO: 从认证中获取
        **widget.model_dump()
    )
    db.add(db_widget)
    await db.commit()
    await db.refresh(db_widget)
    return db_widget

@router.put("/{widget_id}", response_model=WidgetSchema)
async def update_widget(
    widget_id: int,
    widget: WidgetUpdate,
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    result = await db.execute(select(Widget).filter(Widget.id == widget_id))
    db_widget = result.scalar_one_or_none()
    if not db_widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    for field, value in widget.model_dump(exclude_unset=True).items():
        setattr(db_widget, field, value)
    
    await db.commit()
    await db.refresh(db_widget)
    return db_widget

@router.delete("/{widget_id}")
async def delete_widget(
    widget_id: int,
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    result = await db.execute(select(Widget).filter(Widget.id == widget_id))
    db_widget = result.scalar_one_or_none()
    if not db_widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    
    await db.delete(db_widget)
    await db.commit()
    return {"ok": True} 