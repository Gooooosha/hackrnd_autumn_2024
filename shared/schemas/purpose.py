from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PurposeBase(BaseModel):
    purpose_type: str


class PurposeCreate(PurposeBase):
    pass


class PurposeUpdate(BaseModel):
    purpose_type: Optional[str]


class PurposeInDBBase(PurposeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Purpose(PurposeInDBBase):
    pass


class PurposeInDB(PurposeInDBBase):
    pass
