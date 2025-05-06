from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db
from app.schemas.booking import BookingReadSchema
from app.service.booking import BookingService

router = APIRouter(prefix="/bookings", tags=["Бронирования"])


@router.get("/")
async def get_all(
    session: AsyncSession = Depends(db.get_session),
) -> list[BookingReadSchema]:
    return await BookingService.get_all(session)


@router.get("/id")
async def get_by_id(
    id: int, session: AsyncSession = Depends(db.get_session)
) -> BookingReadSchema:
    return await BookingService.get_by_id(session, id=id)
