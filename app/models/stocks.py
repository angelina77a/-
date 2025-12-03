from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.stocks import StocksModel


class RoleModel(Base):
    __tablename__ = "stocks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    family: Mapped[int] = mapped_column(Float, default=0.0)  
    seasonal: Mapped[int] = mapped_column(Integer, nullable=False)
    bonuses: Mapped[int] = mapped_column(Integer, nullable=False)