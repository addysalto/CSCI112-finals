from utils import *
from createScripts import *  # functions: create_user, create_title
from readScripts import *  # functions: fetch_user_watch_history, fetch_recommendations
from updateScripts import *  # functions: track_viewing_progress
from deleteScripts import *  # functions: delete_user, delete_title

def main():
    conn = openConnection()
    db = conn["projectVibes"] 

    try:
        # 1. Create a User
        user_id = create_user(db, "john_doe", "password123", "john@example.com", "USA")
        print(f"User created with ID: {user_id}")

        # 2. Add a Title
        title_id = create_title(
            db, user_id, "Inception", "A mind-bending thriller", 148, ["Sci-Fi"], ["Nolan"]
        )
        print(f"Title created with ID: {title_id}")

        # 3. Fetch User Watch History
        history = fetch_user_watch_history(db, user_id)
        print("Watch History:", history)

        # 4. Get Recommendations
        recommendations = fetch_recommendations(db, user_id)
        print("Recommendations:", recommendations)

        # 5. Update Watch Progress
        track_viewing_progress(db, user_id, title_id, 90, False)
        print("Watch progress updated.")

        # 6. Delete Records
        delete_user(db, user_id)
        delete_title(db, title_id)
        print("User and Title deleted.")
        
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Ensures the connection is closed even if an error occurs
        closeConnection(conn)

if __name__ == "__main__":
    main()
