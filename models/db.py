from dotenv import load_dotenv,find_dotenv
import os 
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())


password_db= os.environ.get("MONGODB_PWD")
connection_string= os.environ.get("MONGODB_CON")
client= MongoClient(connection_string)

def get_db():
    client = MongoClient('connection_string')
    db = client['Movie-review']
    return db
