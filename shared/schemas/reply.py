from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReplyBase(BaseModel):
    reply_text: str


class ReplyCreate(ReplyBase):
    pass


class ReplyUpdate(BaseModel):
    reply_text: Optional[str]


class ReplyInDBBase(ReplyBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Reply(ReplyInDBBase):
    pass


class ReplyInDB(ReplyInDBBase):
    pass
