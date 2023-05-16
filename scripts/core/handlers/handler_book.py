from scripts.utils.mongo_utility import Collection
from scripts.schemas.response_models import Library, Email
from scripts.core.handlers.email_handler import Email_handler


def store_book(book: Library):
    try:
        result = Collection.insert_one(book.__dict__)
        return {"message": f"Book stored successfully "}
    except Exception as e:
        return {"error": str(e)}


def get_book(book_name: str,):
    try:
        book = Collection.find_one({"title": book_name})
        if book:
            return {"message": " book is available"}
        return {"error": "Book not found"}
    except Exception as e:
        return {"error": str(e)}


def update_book(book_name: str, new_book: Library):
    try:
        result = Collection.update_one({"title": book_name}, {"$set": new_book.__dict__})
        if result.modified_count > 0:
            return {"message": "Book updated successfully"}
        return {"error": "Book not found"}
    except Exception as e:
        return {"error": str(e)}


def delete_book(book_name: str):
    try:
        result = Collection.delete_one({"title": book_name})
        if result.deleted_count > 0:
            return {"message": "Book deleted successfully"}
        return {"error": "Book not found"}
    except Exception as e:
        return {"error": str(e)}


def sending_item(email: Email):
    item_object = Email_handler()
    send_items = item_object.send_email(email)
    return "Email sent successfully"
