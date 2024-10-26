from tasks_shared.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from shared.utils.mixins.timestamps_mixin import TimestampMixin


class Editor(Base, TimestampMixin):
    __tablename__ = "editors"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)

    class Config:
        orm_mode = True
        from_attributes = True
