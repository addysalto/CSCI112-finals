from createScripts import * # functions: create_user, create_title, create_watch_history, create_login_log, create_event
from readScripts import * # functions: get_user_by_credentials, get_user_watch_history, get_content_recommendations, search_titles
from updateScripts import * # functions: update_watch_progress, update_title_rating
from deleteScripts import * # functions: delete_user, delete_watch_history, delete_login_log, delete_rating
from utils import * # functions: create_login_data, create_watch_history_data, create_event_data, create_rating_data, create_recommendation_log

def test_create_operations():
    # Test creating a user
    user_data = {
        "username": "john_doe",
        "password": "securepassword",
        "email": "john_doe@example.com"
    }
    user_id = create_user(user_data)

    # Test creating a title
    title_data = {
        "titleName": "Inception",
        "genre": "Sci-Fi",
        "releaseDate": "2010-07-16"
    }
    title_id = create_title(title_data)

    # Test creating watch history
    watch_history_data = create_watch_history_data(user_id, title_id)
    create_watch_history(watch_history_data)

    # Test creating a login log
    login_data = create_login_data(user_id, True)
    create_login_log(login_data)

    # Test creating an event log
    event_data = create_event_data(user_id, "login", "User logged in successfully")
    create_event(event_data)

    

def test_read_operations(username, password):
    # Test reading user by credentials
    user = get_user_by_credentials("john_doe", "securepassword")
    print(user)

    # Test reading watch history
    watch_history = get_user_watch_history(user["_id"])
    print(watch_history)

    # Test content recommendations
    recommendations = get_content_recommendations(user["_id"])
    print(recommendations)

    # Test search for titles
    search_results = search_titles("Inception")
    print(search_results)

def test_update_operations(username, password, title_name):
    user = get_user_by_credentials("john_doe", "securepassword")
    print(user)
    
    title = search_titles(title_name)
    title_id = title[0]["_id"]
    print(title_id, user["_id"])

    # Test updating watch progress
    update_watch_progress(user["_id"], title_id, 120, "completed")

    # Test updating title rating
    update_title_rating(user["_id"], title_id, 5, "Amazing movie!")

def test_delete_operations(username, password, title_name):
    user = get_user_by_credentials("john_doe", "securepassword")
    print(user)

    title = search_titles(title_name)
    title_id = title[0]["_id"]

    user_id = user["_id"]
    # Test deleting user
    delete_user(user["_id"])

    # Test deleting watch history
    delete_watch_history(user["_id"], title_id)

    # Test deleting login logs
    delete_login_log(user["_id"])

    # Test deleting rating
    delete_rating(user["_id"], title_id)

def main():
    username = "john_doe"
    password = "securepassword"
    title_name = "Inception"

    print("Running create operations test...")
    test_create_operations()

    print("\nRunning read operations test...")
    test_read_operations(username, password)

    print("\nRunning update operations test...")
    test_update_operations(username, password, title_name)

    print("\nRunning delete operations test...")
    test_delete_operations(username, password, title_name)

if __name__ == "__main__":
    main()
