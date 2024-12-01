from utils import get_db

def delete_user(user_id):
    db = get_db()
    db.user.delete_one({"_id": user_id})

def delete_title(title_id):
    db = get_db()
    db.title.delete_one({"_id": title_id})
