from pydantic import BaseModel


class DeleteRequest(BaseModel):
    id: int
