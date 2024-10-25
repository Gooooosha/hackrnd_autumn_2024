from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class ClientBase(BaseModel):
    contract_number: str = Field(..., min_length=9, max_length=9)
    name: str
    surname: str
    middle_name: str
    phone_number: str
    email: EmailStr
    address: str
    tg_id: str
    

class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    contract_number: Optional[str] = Field(..., min_length=9, max_length=9)
    name: Optional[str]
    surname: Optional[str]
    middle_name: Optional[str]
    phone_number: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    tg_id: Optional[str]


class ClientInDBBase(ClientBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Client(ClientInDBBase):
    pass


class ClientInDB(ClientInDBBase):
    pass
