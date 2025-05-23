from datetime import date

from sqlalchemy import ForeignKey, text, Integer, Computed
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date]
    date_to: Mapped[date]
    price: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    total_cost: Mapped[int] = mapped_column(
        Integer, Computed("(date_to - date_from) * price")
    )
    total_days: Mapped[int] = mapped_column(Integer, Computed("date_to - date_from"))
