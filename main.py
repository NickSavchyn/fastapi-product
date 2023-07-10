from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_async_session
from routers import products

app = FastAPI()
app.include_router(products.router)


async def get_db() -> AsyncSession:
    async with get_async_session() as db:
        yield db

