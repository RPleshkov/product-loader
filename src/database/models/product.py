from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Product(Base):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(String(350))
    guid: Mapped[str | None] = mapped_column(String(255), unique=True)
    origin: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(String(255))
    origin_url: Mapped[str] = mapped_column(String(255))
    preview_img: Mapped[str | None] = mapped_column(String(255))
    price: Mapped[int] = mapped_column()
    create_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
    )
    update_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
    )
