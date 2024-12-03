from pymongo import MongoClient
from datetime import datetime

def openConnection():
    # MongoDB URI
    url = 'mongodb+srv://grp5:Ra8b2hkQQ7dFiFUv@grp5-csci112-finalproj.n88pt.mongodb.net/'  
    conn = MongoClient(url)
    return conn

def closeConnection(conn):
    conn.close()

def get_current_timestamp():
    # Returns the current timestamp in ISO format
    return datetime.utcnow().isoformat()

def create_login_data(user_id, success):
    # Creates a login log entry
    return {
        "userId": user_id,
        "timestamp": get_current_timestamp(),
        "success": success
    }

def create_watch_history_data(user_id, title_id, time_watched=0, completion_status="incomplete"):
    # Creates watch history data entry
    return {
        "userId": user_id,
        "titleId": title_id,
        "timeWatched": time_watched,
        "completionStatus": completion_status,
        "lastUpdated": get_current_timestamp()
    }

def create_event_data(user_id, event_type, details=None):
    # Creates event log data
    return {
        "userId": user_id,
        "eventType": event_type,
        "details": details,
        "timestamp": get_current_timestamp()
    }

def create_rating_data(user_id, title_id, rating, comment=None):
    # Creates rating data
    return {
        "userId": user_id,
        "titleId": title_id,
        "rating": rating,
        "comment": comment,
        "timestamp": get_current_timestamp()
    }

def create_recommendation_log(user_id, recommendation_data):
    # Creates a recommendation log entry
    return {
        "userId": user_id,
        "recommendationData": recommendation_data,
        "timestamp": get_current_timestamp()
    }
