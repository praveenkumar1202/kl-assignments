from pydantic import BaseModel


class Library(BaseModel):
    id: int
    name: str
    author: str
    quantity: int
