from utils import *
from datetime import datetime

def validate_user_login(username, password):
    db = get_db()
    user = db.user.find_one({"username": username, "password": password})
    status = "success" if user else "failure"
    db.loginLog.insert_one({
        "userId": user["_id"] if user else None,
        "timestamp": datetime.now(),
        "status": status,
    })
    return user

def fetch_user_watch_history(user_id):
    db = get_db()
    history = db.watchHistory.aggregate([
        {"$match": {"userId": user_id}},
        {
            "$lookup": {
                "from": "title",
                "localField": "titleId",
                "foreignField": "_id",
                "as": "titleDetails",
            }
        },
    ])
    db.eventLog.insert_one({
        "userId": user_id,
        "eventId": "view_watch_history",
        "timestamp": datetime.now(),
    })
    return list(history)

def fetch_recommendations(user_id):
    db = get_db()
    history = db.watchHistory.find({"userId": user_id})
    viewed_title_ids = [entry["titleId"] for entry in history]

    # Recommendation logic: Filter titles the user hasn't watched
    recommendations = db.title.find({"_id": {"$nin": viewed_title_ids}}).limit(10)
    
    db.eventLog.insert_one({
        "userId": user_id,
        "eventId": "recommendations_generated",
        "timestamp": datetime.now(),
    })
    return list(recommendations)

def search_titles(query, user_id):
    db = get_db()
    search_results = db.title.find({
        "$or": [
            {"titleName": {"$regex": query, "$options": "i"}},
            {"tags": {"$regex": query, "$options": "i"}},
            {"genre": {"$regex": query, "$options": "i"}}
        ]
    })
    db.contentSearchLog.insert_one({
        "userId": user_id,
        "searchQuery": query,
        "searchedAt": datetime.now(),
        "resultsCount": search_results.count()
    })
    return list(search_results)

def update_recommendation_engine():
    db = get_db()
    pipeline = [
        {"$lookup": {
            "from": "rating",
            "localField": "_id",
            "foreignField": "titleId",
            "as": "ratings",
        }},
        {"$unwind": "$ratings"},
        {"$group": {
            "_id": "$_id",
            "averageRating": {"$avg": "$ratings.rating"},
            "viewCount": {"$sum": "$viewCount"},
        }},
    ]
    recommendations = db.title.aggregate(pipeline)
    return list(recommendations)
