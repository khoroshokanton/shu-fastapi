from fastapi import HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class BaseService:
    model = None

    @classmethod
    async def get_all(cls, session: AsyncSession, **filters):
        stmt = select(cls.model).filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def get_by_id(cls, session: AsyncSession, id: int):
        return await session.get(cls.model, id)

    @classmethod
    async def get_one_or_none(cls, session: AsyncSession, **filters):
        stmt = select(cls.model).filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def create(cls, session: AsyncSession, values: dict[str, any]):
        try:
            stmt = insert(cls.model).values(**values)
            await session.execute(stmt)
            await session.commit()
        except BaseException as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": f"Ошибка при создании пользователя. {e}"},
            )
