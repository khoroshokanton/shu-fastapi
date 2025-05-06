from typing import Any, Text

from sqlalchemy import ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base


class Room(Base):
    __tablename__ = "rooms"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    discription: Mapped[Text] = mapped_column(
        default="",
        server_default=text("''"),
    )
    price: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default=text("0"),
    )
    services: Mapped[dict[str, Any]]
    quantity: Mapped[int] = mapped_column(default=0, server_default=text("0"))
    image_id: Mapped[int]

    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
