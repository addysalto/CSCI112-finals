from pymongo import MongoClient
from datetime import datetime, timedelta
import random

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

def random_date():
    start_date = datetime(2000, 1, 1) 
    end_date = datetime(2024, 12, 4)  

    total_days = (end_date - start_date).days

    random_days = random.randint(0, total_days)

    return start_date + timedelta(days=random_days)

def create_login_data(user_id, success):
    # Creates a login log entry
    return {
        "userId": user_id,
        "timestamp": get_current_timestamp(),
        "success": success
    }

def create_watch_history_data(user_id, title_id, time_watched, completion_status="incomplete", last_updated=None):
    # Creates watch history data entry
    return {
        "userId": user_id,
        "titleId": title_id,
        "timeStopped": time_watched,
        "completionStatus": completion_status,
        "lastUpdated": get_current_timestamp()
    }

def create_eventlg_data(user_id, event_type, details=None):
    # Creates event log data
    return {
        "userId": user_id,
        "event_type": event_type,
        "details": details,
        "timestamp": get_current_timestamp()
    }

def create_searchlg_data(user_id, searchQuery, resultsCount):
    # Creates search log data
    return {
        "userId": user_id,
        "searchQuery": searchQuery,
        "searchedAt": get_current_timestamp(),
        "resultsCount": resultsCount
    }

def create_rating_data(user_id, title_id, rating, comment=None):
    # Creates rating data
    return {
        "userId": user_id,
        "titleId": title_id,
        "rating": rating,
        "comment": comment,
        "lastUpdated": get_current_timestamp()
    }

def create_loginlg_data(user_id, status):
    # Creates login log data
    return {
        "userId": user_id,
        "status": status
    }

def create_recommendationlg_data(user_id, recommendations):
    # Creates a recommendation log entry
    return {
        "userId": user_id,
        "recommendationData": recommendations,
        "timestamp": get_current_timestamp()
    }
