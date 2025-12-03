from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.bookings import BookingsModel


class BookingsModel(Base):
    __tablename__ = "bookings"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    payment: Mapped[int] = mapped_column(Integer, default=0.0)  
    date: Mapped[datetime] = mapped_column(datetime, nullable=False)
    process: Mapped[datetime] = mapped_column(datetime, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    direction: Mapped[int] = mapped_column(Integer, nullable=False)


