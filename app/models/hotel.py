from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String

from app.core.base import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    location: Mapped[str] = mapped_column(String(100))
    services: Mapped[dict[str, Any] | None]
    rooms_quantity: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    image_id: Mapped[int | None]
