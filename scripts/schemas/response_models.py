from pydantic import BaseModel


class Library(BaseModel):
    id: int
    title: str
    author: str
    quantity: int


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str
