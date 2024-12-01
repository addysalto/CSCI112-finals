from utils import get_db
from datetime import datetime

def track_viewing_progress(user_id, title_id, time_stopped, completed):
    db = get_db()
    db.watchHistory.update_one(
        {"userId": user_id, "titleId": title_id},
        {
            "$set": {
                "timeStopped": time_stopped,
                "completionStatus": completed,
                "watchDate": datetime.now(),
            }
        },
        upsert=True,  # Create a new record if it doesn’t exist
    )
