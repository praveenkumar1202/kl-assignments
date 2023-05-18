from scripts.core.handlers.handler_book import store_book, get_book, delete_book, update_book,pipeline_aggregation
from fastapi import APIRouter
from scripts.schemas.response_models import Library, Email
from scripts.constants.app_constant import Apis
from scripts.core.handlers.email_handler import send_email

library_router = APIRouter()


@library_router.post(Apis.create_api)
def books(book: Library):
    try:
        return store_book(book.dict())
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


@library_router.get(Apis.get_api)
def books(book_name: str, book_id: str = None):
    try:
        return get_book(book_name, book_id)
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


@library_router.put(Apis.update_api)
def books(book_name: str, new_book: Library, book_id: str = None):
    try:
        return update_book(book_name, new_book, book_id)
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


@library_router.delete(Apis.delete_api)
def books(book_name: str, book_id: str = None):
    try:
        return delete_book(book_name, book_id)
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


@library_router.post(Apis.email_api)
def books(email: Email):
    try:
        total_quantity = pipeline_aggregation()
        return send_email(email, str(total_quantity))
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


@library_router.get(Apis.total_api)
def books():
    try:
        return pipeline_aggregation()
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}

