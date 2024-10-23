from dotenv import load_dotenv,find_dotenv
import os 
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())


password_db= os.environ.get("MONGODB_PWD")
connection_string= os.environ.get("MONGODB_CON")
client= MongoClient(connection_string)

def get_db1():
    client = MongoClient('connection_string')
    db = client['Movie-review']
    return db


def get_db():
    # Connect to MongoDB server (localhost for this example)
    client = MongoClient('mongodb+srv://simrn204:Ottawa2004@simran1993.rc2c4.mongodb.net/')
    # Access or create the movie_reviews database
    db = client['movie_reviews']
    return db
