from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.subscriptions import SubscriptionsModel


class SubscriptionsModel(Base):
    __tablename__ = "subscriptions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    year: Mapped[int] = mapped_column(Float, default=0.0)  
    month: Mapped[int] = mapped_column(Integer, nullable=False)
    week: Mapped[int] = mapped_column(Integer, nullable=False)