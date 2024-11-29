from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.db.base import get_db
from backend.app.models.todo import Todo
from backend.app.schemas.todo import TodoCreate, TodoUpdate, Todo as TodoSchema

router = APIRouter()

@router.get("/", response_model=List[TodoSchema])
async def get_todos(
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    result = await db.execute(select(Todo))
    todos = result.scalars().all()
    return todos

@router.post("/", response_model=TodoSchema)
async def create_todo(
    todo: TodoCreate,
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    db_todo = Todo(
        # user_id=current_user.id,  # TODO: 从认证中获取
        **todo.model_dump()
    )
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo

@router.put("/{todo_id}", response_model=TodoSchema)
async def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    result = await db.execute(select(Todo).filter(Todo.id == todo_id))
    db_todo = result.scalar_one_or_none()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    for field, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, field, value)
    
    await db.commit()
    await db.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db),
    # TODO: 添加用户认证
):
    result = await db.execute(select(Todo).filter(Todo.id == todo_id))
    db_todo = result.scalar_one_or_none()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await db.delete(db_todo)
    await db.commit()
    return {"ok": True} 