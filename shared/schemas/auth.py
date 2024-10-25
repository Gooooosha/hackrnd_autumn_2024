from pydantic import BaseModel, Field, EmailStr


class Contract(BaseModel):
    contract_number: str = Field(..., min_length=9, max_length=9)


class AuthCode(BaseModel):
    code: str = Field(..., min_length=4, max_length=4)
