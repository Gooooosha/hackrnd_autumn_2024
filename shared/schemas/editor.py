from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EditorAddRequest(BaseModel):
    login: str
    password: str
    role: str


class EditorBase(BaseModel):
    login: str
    hashed_password: str
    role: str


class EditorCreate(EditorBase):
    pass


class EditorUpdate(BaseModel):
    login: Optional[str]
    hashed_password: Optional[str]
    role: Optional[str]


class EditorInDBBase(EditorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Editor(EditorInDBBase):
    pass


class EditorInDB(EditorInDBBase):
    pass
