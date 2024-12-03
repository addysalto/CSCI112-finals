# Establish the connection to the database

from pymongo import MongoClient
from datetime import datetime

def openConnection():
   url = 'mongodb+srv://grp5:Ra8b2hkQQ7dFiFUv@grp5-csci112-finalproj.n88pt.mongodb.net/' 
   conn = MongoClient(url)
   return conn 

def closeConnection(conn):
    conn.close()
