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

def create_rating(rating_data):
    conn = openConnection()
    db = conn['projectVibes'] 
    ratings_collection = db['rating']
    result = ratings_collection.insert_one(rating_data)
    print(f"Rating created with id: {result.inserted_id}")
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

def create_search_log(search_data):
    conn = openConnection()
    db = conn['projectVibes']  
    event_collection = db['contentSearchLog']
    result = event_collection.insert_one(search_data)
    print(f"Search log created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id

def create_event_log(eventlg_data):
    conn = openConnection()
    db = conn['projectVibes']  
    event_collection = db['eventLog']
    result = event_collection.insert_one(eventlg_data)
    print(f"Event log created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id

def create_recommendation_log(recommendationlg_data):
    conn = openConnection()
    db = conn['projectVibes']  
    event_collection = db['recommendationLog']
    result = event_collection.insert_one(recommendationlg_data)
    print(f"Recommendation log created with id: {result.inserted_id}")
    closeConnection(conn)
    return result.inserted_id


# Login: Check credentials and create login log
def login(username, password):
    conn = openConnection()
    db = conn['projectViber']
    userCollection = db['user']
    
    user = userCollection.find_one({'username': username})

    if user:
        if user['password'] == password:
            login_data = create_loginlg_data(user['_id'], True)
            login_log = create_login_log(login_data)
            print("Login successful.")
            return login_log
        else:
            login_data = create_loginlg_data(user['_id', False])
            login_log = create_login_log(login_data)
            print("Login failed: Invalid password.")
            return login_log
    else:
        login_data = create_loginlg_data(None, False)
        login_log = create_login_log(login_data)
        print("Login failed: Invalid username")
        return login_log
