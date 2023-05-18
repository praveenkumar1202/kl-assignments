from scripts.core.handlers.email_handler import send_email
from scripts.schemas.response_models import Library, Email
from scripts.utils.mongo_utility import Collection

import uuid


def store_book(book):
    try:
        result = Collection.insert_one(book)
        return {"message": "Book stored successfully", "status": "success"}
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg), "status": "failed"}


def get_book(book_name: str, book_id: str = None):
    try:
        book = Collection.find_one({"title": book_name, "id": book_id})
        if book:
            return {"message": " book is available", "details": list(book), "status": "success"}
        return {"error": "Book not found", "status": "failed"}
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


def update_book(book_name: str, new_book: Library, book_id: str = None):
    try:
        result = Collection.update_one({"title": book_name, "_id": book_id}, {"$set": new_book.__dict__})
        if result.modified_count > 0:
            return {"message": "Book updated successfully", "status": "success"}
        return {"error": "Book not found", "status": "failed"}
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


def delete_book(book_name: str, book_id: str):
    try:
        result = Collection.delete_one({"title": book_name, "_id": book_id})
        if result.deleted_count > 0:
            return {"message": "Book deleted successfully", "status": "success"}
        return {"error": "Book not found", "status": "failed"}
    except Exception as exceptionMsg:
        return {"error": str(exceptionMsg)}


def pipeline_aggregation():
    pipeline = [
        {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$quantity'
                },
                'count': {'$sum': 1}
            }
        },
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = Collection.aggregate(pipeline)
    data = list(data)
    print(data)
    return {"total books in library": data[0]['total']}
