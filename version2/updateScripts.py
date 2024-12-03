from pymongo import MongoClient
from utils import *

def update_watch_progress(user_id, title_id, time_stopped, completion_status):
    conn = openConnection()
    db = conn['projectVibes']  
    watch_history_collection = db['watchHistory']
    
    # Find and update the watch history for the given user and title
    result = watch_history_collection.update_one(
        {"userId": user_id, "titleId": title_id},
        {"$set": {"timeStopped": time_stopped, "completionStatus": completion_status}}
    )
    print(f"Watch progress updated: {result.modified_count} document(s) updated.")
    closeConnection(conn)
    return result.modified_count

def update_title_rating(user_id, title_id, rating, comment=None):
    conn = openConnection()
    db = conn['projectVibes']  
    ratings_collection = db['rating']
    
    # Check if the user has already rated the title, if yes, update it.
    result = ratings_collection.update_one(
        {"userId": user_id, "titleId": title_id},
        {"$set": {"rating": rating, "comment": comment}},
        upsert=True  # If the rating does not exist, it will create a new one
    )
    print(f"Rating updated: {result.modified_count} document(s) updated.")
    closeConnection(conn)
    return result.modified_count
