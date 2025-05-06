from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

from .config import settings


class DatabaseManager(DeclarativeBase):
    def __init__(self, echo: bool = False):
        self.engine: AsyncEngine = create_async_engine(str(settings.db.url), echo=echo)

        self.session_factory = async_sessionmaker(
            self.engine, expire_on_commit=False, autoflush=False
        )

    async def engine_dispose(self):
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db = DatabaseManager()
