from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

Base = declarative_base()

class Database:
    def __init__(self, database_url: str, echo: bool = False):
        self.engine = create_async_engine(database_url, echo=echo)
        self.session_local = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    @asynccontextmanager
    async def get_session(self):
        async with self.session_local() as session:
            yield session

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def dispose(self):
        await self.engine.dispose()

db = Database(settings.db.get_url())