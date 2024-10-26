from tasks_shared.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from shared.utils.mixins.timestamps_mixin import TimestampMixin
from pydantic import EmailStr


class Client(Base, TimestampMixin):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    contract_number: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str | None] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[EmailStr] = mapped_column(nullable=False, unique=True)
    address: Mapped[str] = mapped_column(nullable=False, unique=True)
    tg_id: str = mapped_column(nullable=False, unique=True)

    class Config:
        orm_mode = True
        from_attributes = True
