from pymongo import MongoClient
from utils import *
from createScripts import *
from datetime import datetime

def get_user_by_credentials(username, password):
    conn = openConnection()
    db = conn['projectVibes']  
    users_collection = db['user']
    user = users_collection.find_one({"username": username, "password": password})
    closeConnection(conn)
    return user

def get_user_watch_history(user_id):
    conn = openConnection()
    db = conn['projectVibes']  
    watch_history_collection = db['watchHistory']
    watch_history = watch_history_collection.find({"userId": user_id})
    list_watch_history = list(watch_history)
    closeConnection(conn)
    return list_watch_history

def get_content_recommendations(user_id):
    conn = openConnection()
    db = conn['projectVibes']  
    watch_history_collection = db['watchHistory']
    ratings_collection = db['rating']
    titles_collection = db['title']

    # Aggregate user's watch history and ratings to build recommendations
    pipeline = [
        {"$match": {"userId": user_id}},
        {"$lookup": {
            "from": "title",
            "localField": "titleId",
            "foreignField": "_id",
            "as": "title_details"
        }},
        {"$lookup": {
            "from": "rating",
            "localField": "titleId",
            "foreignField": "titleId",
            "as": "ratings"
        }},
        {"$project": {
            "titleId": 1, 
            "title_details.titleName": 1, 
            "ratings.rating": 1
        }},
        {"$sort": {"ratings.rating": -1}}
    ]

    recommendations = watch_history_collection.aggregate(pipeline)
    list_recommendations = list(recommendations)
    closeConnection(conn)
    return list_recommendations

def search_titles(user_id, query):
    conn = openConnection()
    db = conn['projectVibes']  
    titles_collection = db['title']
    search_result = titles_collection.find({"titleName": {"$regex": query, "$options": 'i'}})
    list_search_result = list(search_result)
    resultCount = len(list_search_result)
    searchlg = create_searchlg_data(user_id, query, resultCount)
    create_search_log(searchlg)
    closeConnection(conn)
    return list_search_result

def get_user_login_logs(user_id):
    conn = openConnection()
    db = conn['projectVibes']  
    login_log_collection = db['loginLog']
    login_logs = login_log_collection.find({"userId": user_id})
    list_login_logs = list(login_logs)
    closeConnection(conn)
    return list_login_logs


