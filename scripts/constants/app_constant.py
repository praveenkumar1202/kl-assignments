class Apis:
    create_api = '/add_books'
    get_api = '/get_book_by_name/{book_name}'
    update_api = '/update_book/{book_name}'
    delete_api = '/delete_book_by_name/{book_name}'
    email_api = '/send_email'
    total_api = '/total_quanty'


class DataBase:
    data_uri = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
    data_name = "interns_b2_23"
    data_collection = "praveen_kumar"
