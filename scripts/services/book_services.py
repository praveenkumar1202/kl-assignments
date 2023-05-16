from scripts.core.handlers.handler_book import store_book, get_book, delete_book, update_book, sending_item
from fastapi import APIRouter
from scripts.schemas.response_models import Library , Email

library_router = APIRouter()


@library_router.post("/add books")
def books(book: Library):
    return store_book(book)


@library_router.get("/get-book-by-name/{book_name}")
def books(book_name: str,):
    return get_book(book_name)


@library_router.put("/update-book/{book_name}")
def books(book_name: str, new_book: Library):
    return update_book(book_name, new_book)


@library_router.delete("/delete-book-by-name/{book_name}")
def books(book_name: str):
    return delete_book(book_name)


@library_router.post("/send_email")
def fun(email: Email):
    return sending_item(email)
