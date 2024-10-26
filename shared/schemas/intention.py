from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class IntentionBase(BaseModel):
    keyword: str
    purpose_id: int
    reply_id: int
    

class IntentionCreate(IntentionBase):
    pass


class IntentionUpdate(BaseModel):
    keyword: Optional[str]
    purpose_id: Optional[int]
    reply_id: Optional[int]


class IntentionInDBBase(IntentionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Intention(IntentionInDBBase):
    pass


class IntentionInDB(IntentionInDBBase):
    pass
