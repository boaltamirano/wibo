from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

def get_database():
    client = MongoClient(MONGO_URI)
    db = client.get_database(os.getenv("DATABASE"))
    return db