import enum
from datetime import datetime
from sqlalchemy import String, Column
from sqlalchemy.orm import Mapped, mapped_column
from core.data.database import Base


class AnimalType(enum.Enum):
    cat = "cat"
    dog = "dog"


class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(String(30), nullable=False)
    type: Mapped[AnimalType]
    created_at: Mapped[str] = mapped_column(nullable=False, default=datetime.now().isoformat(timespec='seconds'))
    updated_at: Mapped[str | None] = mapped_column(default=None,
                                                   onupdate=datetime.now().isoformat(timespec='seconds'))
