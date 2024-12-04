from createScripts import * # functions: create_user, create_title, create_watch_history, create_login_log, create_event
from readScripts import * # functions: get_user_by_credentials, get_user_watch_history, get_content_recommendations, search_titles
from updateScripts import * # functions: update_watch_progress, update_title_rating
from deleteScripts import * # functions: delete_user, delete_watch_history, delete_login_log, delete_rating
from utils import * # functions: create_login_data, create_watch_history_data, create_event_data, create_rating_data, create_recommendation_log

def test_create_operations():
    # Test creating a user
    user_data = {
        "username": "Dexter",
        "password": "dexterdomingo123",
        "email": "dex_123@daido.com",
        "dateCreated": random_date(),
        "userCountry": "Philippines",
    }
    user_id = create_user(user_data)

    # Test creating a title
    title_data = {
        "titleName": "Spider-Man: Beyond the Spider-Verse",
        "titleDescription": "The last of the spider verse series",
        "uploadDate": random_date(),
        "duration": 150,
        "titleType": "Movie",
        "viewCount": 9196236,
        "ratingAverage": 4.8713,
        "ratingCount": 98893,
        "totalWatchTime": 376822876,
        "dateReleased": random_date(),
        "genre": [
        "Action",
        "Western"
        ],
        "tags": [
        "Cyberpunk",
        "FantasyAdventure",
        "Coming-of-Age",
        "Romance"
        ]
    }
    title_id = create_title(title_data)

    # Test creating watch history
    watch_history_data = create_watch_history_data(user_id, title_id, random.randint(0,240), completion_status=random.choice(["complete", "incomplete"]))
    create_watch_history(watch_history_data)

    # Test creating a login log
    login_data = create_loginlg_data(user_id, True)
    create_login_log(login_data)

    # Test creating a rating
    rating_data = create_rating_data(user_id, title_id, random.uniform(0,5))
    create_rating(rating_data)

    # Test creating a search log
    search_data = create_searchlg_data(user_id, "spider", random.randint(1,10))
    create_search_log(search_data)

    # Test creating an event log
    event_data = create_eventlg_data(user_id, "login", "User logged in successfully")
    create_event(event_data)

    # Test creating a recommendation log
    recommendation_data = create_recommendationlg_data(user_id, ["sample_id_1", "sample_id_2", "sample_id_3"])
    create_recommendation_log(recommendation_data)

    

def test_read_operations(username, password, title_name):
    # Test reading user by credentials
    user = get_user_by_credentials(username, password)
    print(user)

    # Test reading watch history
    watch_history, event_log_id = get_user_watch_history(user["_id"])
    print("\nRunning get watch history test...")
    print(watch_history)
    print(event_log_id)
    print("Watch history test end...\n") 

    # Test content recommendations
    recommendations = get_content_recommendations(user["_id"])
    print(recommendations)

    # Test search for titles
    search_results = search_titles(user["_id"], title_name)
    print(search_results)

def test_update_operations(username, password, title_name):
    user = get_user_by_credentials(username, password)
    print(user)
    
    title = search_titles(title_name)
    title_id = title[0]["_id"]
    print(title_id, user["_id"])

    # Test updating watch progress
    update_watch_progress(user["_id"], title_id, 120, "completed")

    # Test updating title rating
    update_title_rating(user["_id"], title_id, 5, "Amazing movie!")

def test_delete_operations(username, password, title_name):
    user = get_user_by_credentials(username, password)
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
    username = "Dexter"
    password = "dexterdomingo123"
    title_name = "Spider-Man: Beyond the Spider-Verse"
    
    #print("Running create operations test...")
    #test_create_operations()
    
    print("\nRunning read operations test...")
    test_read_operations(username, password, title_name)
    '''
    print("\nRunning update operations test...")
    test_update_operations(username, password, title_name)
    '''

    print("\nRunning login test...")
    login(username, password)
    login(username, "wrong_password")
    login("wrong_username", password)

    #print("\nRunning delete operations test...")
    #test_delete_operations(username, password, title_name)

    

if __name__ == "__main__":
    main()
