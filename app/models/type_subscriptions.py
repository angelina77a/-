from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.type_subscriptions import Type_subscriptionsModel


class Type_subscriptionsModel(Base):
    __tablename__ = "type_subscriptions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    user: Mapped[int] = mapped_column(Integer, default=0.0)  
    term: Mapped[int] = mapped_column(Integer, nullable=False)