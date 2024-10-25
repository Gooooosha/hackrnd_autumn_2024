from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    contract_number: str = Field(..., min_length=9, max_length=9)
    first_name: str
    last_name: str
    middle_name: str
    phone_number: str
    description: str
