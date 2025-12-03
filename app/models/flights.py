from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.flights import FlightsModel


class FlightsModel(Base):
    __tablename__ = "flights"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    price: Mapped[int] = mapped_column(float, default=0.0)  
    date: Mapped[datetime] = mapped_column(datetime, nullable=False)
    time: Mapped[datetime] = mapped_column(datetime, nullable=False)
    plane: Mapped[int] = mapped_column(Integer, nullable=False)
    paces: Mapped[int] = mapped_column(Integer, nullable=False)
    booking_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)

booking: Mapped["FlightsModel"] = relationship(back_populates="booking")
