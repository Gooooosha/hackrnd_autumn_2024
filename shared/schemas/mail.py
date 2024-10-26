from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class MailBase(BaseModel):
    mail: EmailStr


class MailCreate(MailBase):
    pass


class MailUpdate(BaseModel):
    mail: Optional[EmailStr]


class MailInDBBase(MailBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Mail(MailInDBBase):
    pass


class MailInDB(MailInDBBase):
    pass
