from dotenv import load_dotenv,find_dotenv
import os 
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())


password_db= os.environ.get("MONGODB_PWD")
connection_string= os.environ.get("MONGODB_CON")
client= MongoClient(connection_string)

dbs=client.list_database_names()
print(dbs)
test_db = client.test 
collections= test_db.list_collection_names()
print(collections)

def test_db():
    collections= test_db.test
    