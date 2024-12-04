from pymongo import MongoClient
from utils import *

def delete_user(user_id):
    conn = openConnection()
    db = conn['projectVibes']  
    users_collection = db['user']
    result = users_collection.delete_one({"_id": user_id})
    print(f"User deleted: {result.deleted_count} document(s) deleted.")
    closeConnection(conn)
    return result.deleted_count

def delete_title(title_id):
    conn = openConnection()
    db = conn['projectVibes']  
    users_collection = db['title']
    result = users_collection.delete_one({"_id": title_id})
    print(f"User deleted: {result.deleted_count} document(s) deleted.")
    closeConnection(conn)
    return result.deleted_count

def delete_watch_history(user_id, title_id):
    conn = openConnection()
    db = conn['projectVibes'] 
    watch_history_collection = db['watchHistory']
    result = watch_history_collection.delete_one({"userId": user_id, "titleId": title_id})
    print(f"Watch history deleted: {result.deleted_count} document(s) deleted.")
    closeConnection(conn)
    return result.deleted_count

def delete_login_log(user_id):
    conn = openConnection()
    db = conn['projectVibes'] 
    login_log_collection = db['loginLog']
    result = login_log_collection.delete_many({"userId": user_id})
    print(f"Login logs deleted: {result.deleted_count} document(s) deleted.")
    closeConnection(conn)
    return result.deleted_count

def delete_rating(user_id, title_id):
    conn = openConnection()
    db = conn['projectVibes']  
    ratings_collection = db['rating']
    result = ratings_collection.delete_one({"userId": user_id, "titleId": title_id})
    print(f"Rating deleted: {result.deleted_count} document(s) deleted.")
    closeConnection(conn)
    return result.deleted_count

def delete_search_log(search_log_id):
    conn = openConnection()
    db = conn['projectVibes']  
    ratings_collection = db['searchLog']
    result = ratings_collection.delete_one({"userId": user_id, "titleId": title_id})
    print(f"Rating deleted: {result.deleted_count} document(s) deleted.")
    closeConnection(conn)
    return result.deleted_count