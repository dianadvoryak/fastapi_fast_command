from fastapi import APIRouter
from sqlalchemy import select
from src.models.books import BookModel
from src.api.dependencies import SessionDep
from src.schemas.books import BookAddSchema
from src.database import engine, Base

db = APIRouter(prefix="/database", tags=["DB"])


@db.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"success": True}

@db.post("/books")
async def add_book(data: BookAddSchema, session: SessionDep):
    new_book = BookModel(title=data.title, author=data.author,)
    session.add(new_book)
    await session.commit()
    return {"success": True}

@db.get("/books")
async def get_book(session: SessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    return result.scalars().all()