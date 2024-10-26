from tasks_shared.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from shared.utils.mixins.timestamps_mixin import TimestampMixin


class Intention(Base, TimestampMixin):
    __tablename__ = "intentions"

    id: Mapped[int] = mapped_column(primary_key=True)
    keyword: Mapped[str] = mapped_column(nullable=False)
    purpose_id: Mapped[int] = mapped_column(ForeignKey("purposes.id", ondelete="cascade"))
    reply_id: Mapped[int] = mapped_column(ForeignKey("replies.id", ondelete="cascade"))
    mail_id: Mapped[int] = mapped_column(ForeignKey("mails.id", ondelete="cascade"))

    class Config:
        orm_mode = True
        from_attributes = True
