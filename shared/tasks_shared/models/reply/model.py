from tasks_shared.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from shared.utils.mixins.timestamps_mixin import TimestampMixin


class Reply(Base, TimestampMixin):
    __tablename__ = "replies"

    id: Mapped[int] = mapped_column(primary_key=True)
    reply_text: Mapped[str] = mapped_column(nullable=False)

    class Config:
        orm_mode = True
        from_attributes = True
