from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine(
    "postgresql+asyncpg://hiro@localhost/history",
    echo=True,
)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
