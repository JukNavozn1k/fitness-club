# database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings 

Base = declarative_base()

# Создаём engine для основной (боевой) БД.
engine = create_async_engine(settings.db.get_url(), echo=False)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Зависимость для получения сессии основной БД.
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session