from pymongo import MongoClient
from datetime import datetime
from utils import *

def create_user(user_data):
    conn = openConnection()
    db = conn['projectVibes']  
    users_collection = db['user']
    result = users_collection.insert_one(user_data)
    print(f"User created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id

def create_title(title_data):
    conn = openConnection()
    db = conn['projectVibes']  
    titles_collection = db['title']
    result = titles_collection.insert_one(title_data)
    print(f"Title created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id

def create_watch_history(watch_history_data):
    conn = openConnection()
    db = conn['projectVibes']  
    watch_history_collection = db['watchHistory']
    result = watch_history_collection.insert_one(watch_history_data)
    print(f"Watch history created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id

def create_login_log(login_data):
    conn = openConnection()
    db = conn['projectVibes']  
    login_log_collection = db['loginLog']
    result = login_log_collection.insert_one(login_data)
    print(f"Login log created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id

def create_event(event_data):
    conn = openConnection()
    db = conn['projectVibes']  
    event_collection = db['event']
    result = event_collection.insert_one(event_data)
    print(f"Event created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id
