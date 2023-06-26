from dotenv import load_dotenv
import os

from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        load_dotenv()
        self.string_connection = os.getenv("MONGODB_STRING_CONNECTION")
        self.database = os.getenv("MONGODB_DATABASE")
        self.collection_name = os.getenv("MONGODB_COLLECTION")
        self.__get_connection()

    def __get_connection(self):
        client = MongoClient(self.string_connection)
        database = client[self.database]
        self.collection = database[self.collection_name]

    def get_data(self, criterial):
        return self.collection.find(criterial)
