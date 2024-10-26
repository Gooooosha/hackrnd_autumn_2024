from pydantic import BaseModel, Field


class Contract(BaseModel):
    contract_number: str = Field(..., min_length=9, max_length=9)


class AuthCode(BaseModel):
    code: str = Field(..., min_length=4, max_length=4)


class Login(BaseModel):
    login: str = Field(..., min_length=1, max_length=255)
    password: str = Field(..., min_length=8, max_length=255)
