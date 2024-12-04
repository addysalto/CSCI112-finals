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

    # Create event log to track watch history access
    eventlg_data = create_eventlg_data(user_id, "watch_history_access")
    event_log_id = create_event_log(eventlg_data)
    return list_watch_history, event_log_id

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
    event = "recommendations generated"
    eventlg = create_eventlg_data(user_id, event)
    create_event_log(eventlg)
    closeConnection(conn)
    return list_recommendations

def search_titles(user_id, query):
    conn = openConnection()
    db = conn['projectVibes']  
    titles_collection = db['title']
    search_result = titles_collection.find({"titleName": {"$regex": query, "$options": 'i'}})
    list_search_result = list(search_result)
    resultCount = len(list_search_result)
    closeConnection(conn)
    searchlg = create_searchlg_data(user_id, query, resultCount)
    create_search_log(searchlg)
    return list_search_result

def get_title_id_by_name(title_name):
    conn = openConnection()
    db = conn['projectVibes']  
    titles_collection = db['title']
    title_id = titles_collection.find_one({"titleName": title_name})
    closeConnection(conn)
    return title_id

def get_user_login_logs(user_id):
    conn = openConnection()
    db = conn['projectVibes']  
    login_log_collection = db['loginLog']
    login_logs = login_log_collection.find({"userId": user_id})
    list_login_logs = list(login_logs)
    closeConnection(conn)
    return list_login_logs

def get_most_viewed_videos_by_genre(genre, n):
    conn = openConnection()
    db = conn['projectVibes']  
    titles_collection = db['title']

    pipeline = [
        {
            "$unwind": "$genres"
        },
        {
            "$match": {"genres": genre}
        },
        {
            "$project": {
                "_id": 1,
                "titleName": 1,
                "viewCount": 1,
            }
        },
        {
            "$sort": { "viewCount": -1 }
        },
        {
            "$limit": n
        },
    ]

    n_most_viewed = titles_collection.aggregate(pipeline)
    list_most_viewed = list(n_most_viewed)
    closeConnection()
    return list_most_viewed

def get_user_statistics(user_id):
    conn = openConnection()
    db = conn['projectVibes']  
    watch_history_collection = db['watchHistory']
    ratings_collection = db['rating']

    # Aggregate user's watch history and ratings to build recommendations
    watch_history_pipeline = [
        {
            "$match": {"userId": user_id} 
        },
        {
            "$group": {
                "_id": "$userId",
                "totalWatchTime": { "$sum": "$timeStopped"} ,
                "numShowsWatched": { "$sum": 1 }
            }
        },
        {
            "$project": {
                "_id": 0,  # Exclude userId from the output
                "totalWatchTime": 1,
                "numShowsWatched": 1,
            }
        }
    ]

    ratings_pipeline = [
        {
            "$match": {"userId": user_id} 
        },
        {
            "$group": {
                "_id": "$userId",
                "numRatingsMade": {"$sum": 1}, 
                "avgRating": {"$avg": "$rating"} 
            }
        },
        {
            "$project": {
                "_id": 0,  
                "numRatingsMade": 1,
                "avgRating": 1
            }
        }
    ]

    watch_history_stats = list(watch_history_collection.aggregate(watch_history_pipeline))
    ratings_stats = list(ratings_collection.aggregate(ratings_pipeline))

    res = {}
    res.update(watch_history_stats[0])
    res.update(ratings_stats[0])

    closeConnection(conn)
    return res



