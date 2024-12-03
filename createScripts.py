from pymongo import MongoClient
from utils import *
from datetime import datetime

def create_user(username, password, email, user_country):
    db = get_db()
    user = {
        "username": username,
        "password": password,
        "email": email,
        "dateCreated": datetime.now(),
        "userCountry": user_country,
    }
    result = db.user.insert_one(user)
    return result.inserted_id

def create_title(user_id, title_name, description, duration, genre, tags):
    db = get_db()
    title = {
        "titleName": title_name,
        "titleDescription": description,
        "uploadDate": datetime.now(),
        "duration": duration,
        "titleType": "Movie",  # Example
        "viewCount": 0,
        "ratingAverage": 0.0,
        "ratingCount": 0,
        "totalWatchTime": 0,
        "dateReleased": datetime.now(),
        "genre": genre,
        "tags": tags,
    }
    result = db.title.insert_one(title)
    return result.inserted_id

def submit_rating(user_id, title_id, rating, comment=None):
    db = get_db()
    db.rating.insert_one({
        "userId": user_id,
        "titleId": title_id,
        "rating": rating,
        "comment": comment,
        "timestamp": datetime.now(),
    })

    # Update the title's rating stats
    title = db.title.find_one({"_id": title_id})
    new_rating_count = title["ratingCount"] + 1
    new_avg_rating = (
        (title["ratingAverage"] * title["ratingCount"] + rating) / new_rating_count
    )
    db.title.update_one(
        {"_id": title_id},
        {"$set": {"ratingAverage": new_avg_rating, "ratingCount": new_rating_count}}
    )

