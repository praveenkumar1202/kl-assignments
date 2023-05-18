from pymongo import MongoClient
from scripts.constants.app_constant import DataBase
client = MongoClient(DataBase.data_uri)
db = client[DataBase.data_name]
Collection = db[DataBase.data_collection]
