from dotenv import load_dotenv,find_dotenv
import os 
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())


connection_string= "mongodb+srv://simrn204:Ottawa2004@simran1993.rc2c4.mongodb.net/"
client= MongoClient(connection_string)

dbs=client.list_database_names()
print(dbs)
