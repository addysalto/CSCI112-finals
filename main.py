from createScripts import * # functions: create_user, create_title
from readScripts import * # functions: fetch_user_watch_history, fetch_recommendations
from updateScripts import * # functions: track_viewing_progress
from deleteScripts import * # functions: delete_user, delete_title

def main():
    # 1. Create a User
    user_id = create_user("john_doe", "password123", "john@example.com", "USA")
    print(f"User created with ID: {user_id}")
    
    # 2. Add a Title
    title_id = create_title(
        user_id, "Inception", "A mind-bending thriller", 148, ["Sci-Fi"], ["Nolan"]
    )
    print(f"Title created with ID: {title_id}")
    
    # 3. Fetch User Watch History
    history = fetch_user_watch_history(user_id)
    print("Watch History:", history)
    
    # 4. Get Recommendations
    recommendations = fetch_recommendations(user_id)
    print("Recommendations:", recommendations)
    
    # 5. Update Watch Progress
    track_viewing_progress(user_id, title_id, 90, False)
    print("Watch progress updated.")
    
    # 6. Delete Records
    delete_user(user_id)
    delete_title(title_id)
    print("User and Title deleted.")

if __name__ == "__main__":
    main()
