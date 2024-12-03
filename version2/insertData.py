from createScripts import * # functions: create_user, create_title, create_watch_history, create_login_log, create_event
from readScripts import * # functions: get_user_by_credentials, get_user_watch_history, get_content_recommendations, search_titles
from updateScripts import * # functions: update_watch_progress, update_title_rating
from deleteScripts import * # functions: delete_user, delete_watch_history, delete_login_log, delete_rating
from utils import * # functions: create_login_data, create_watch_history_data, create_event_data, create_rating_data, create_recommendation_log

user_data = [
  {
    "username": "Mercedes",
    "password": 1310063,
    "email": "wildernoble@daido.com",
    "userCountry": "Svalbard and Jan Mayen Islands"
  },
  {
    "username": "Mitzi",
    "password": 5195826,
    "email": "marisolguy@pearlessa.com",
    "userCountry": "Liechtenstein"
  },
  {
    "username": "Mooney",
    "password": 6551492,
    "email": "greerrodriquez@zoxy.com",
    "userCountry": "Turkey"
  },
  {
    "username": "Keri",
    "password": 5114980,
    "email": "elbaemerson@evidends.com",
    "userCountry": "Gabon"
  },
  {
    "username": "Frieda",
    "password": 9867396,
    "email": "boylechristensen@mazuda.com",
    "userCountry": "Russian Federation"
  }
]

title_data = [
  {
    "titleName": "Spider-Man: Into the Spider-Verse",
    "titleDescription": "placeholder",
    "uploadDate": "Thu Apr 10 1997 19:29:13 GMT+0800 (Philippine Standard Time)",
    "duration": 106,
    "titleType": "Movie",
    "viewCount": 9196236,
    "ratingAverage": 4.8713,
    "ratingCount": 98893,
    "totalWatchTime": 376822876,
    "dateReleased": "Mon Oct 20 1986 15:55:42 GMT+0800 (Philippine Standard Time)",
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
  },
  {
    "titleName": "The Prestige",
    "titleDescription": "placeholder",
    "uploadDate": "Tue Jan 12 2016 06:50:36 GMT+0800 (Philippine Standard Time)",
    "duration": 194,
    "titleType": "Movie",
    "viewCount": 4706141,
    "ratingAverage": 3.2149,
    "ratingCount": 24459,
    "totalWatchTime": 239257772,
    "dateReleased": "Sat May 18 1996 23:12:40 GMT+0800 (Philippine Standard Time)",
    "genre": [
      "Superhero",
      "Science Fiction"
    ],
    "tags": [
      "Heist",
      "RealityTV",
      "Action",
      "Mystery"
    ]
  },
  {
    "titleName": "Guardians of the Galaxy",
    "titleDescription": "placeholder",
    "uploadDate": "Sun Sep 08 2024 21:56:49 GMT+0800 (Philippine Standard Time)",
    "duration": 108,
    "titleType": "Series",
    "viewCount": 6424191,
    "ratingAverage": 1.0382,
    "ratingCount": 48197,
    "totalWatchTime": 560204239,
    "dateReleased": "Wed Jun 17 2020 17:02:18 GMT+0800 (Philippine Standard Time)",
    "genre": [
      "Musical",
      "Mystery"
    ],
    "tags": [
      "Zombies",
      "Historical",
      "War",
      "Werewolves"
    ]
  },
  {
    "titleName": "Toy Story",
    "titleDescription": "placeholder",
    "uploadDate": "Sat Nov 11 2017 14:52:59 GMT+0800 (Philippine Standard Time)",
    "duration": 98,
    "titleType": "Documentary",
    "viewCount": 8208813,
    "ratingAverage": 0.2858,
    "ratingCount": 11868,
    "totalWatchTime": 664269654,
    "dateReleased": "Wed Sep 26 2018 14:14:46 GMT+0800 (Philippine Standard Time)",
    "genre": [
      "Documentary",
      "Musical"
    ],
    "tags": [
      "RealityTV",
      "PostApocalyptic",
      "Science Fiction",
      "Teen"
    ]
  },
  {
    "titleName": "12 Angry Men",
    "titleDescription": "placeholder",
    "uploadDate": "Wed Dec 31 1975 11:25:37 GMT+0800 (Philippine Standard Time)",
    "duration": 162,
    "titleType": "Movie",
    "viewCount": 7623576,
    "ratingAverage": 0.046,
    "ratingCount": 44533,
    "totalWatchTime": 204598340,
    "dateReleased": "Sat Nov 16 2019 06:46:36 GMT+0800 (Philippine Standard Time)",
    "genre": [
      "Drama",
      "Thriller"
    ],
    "tags": [
      "FantasyComedy",
      "Crime",
      "Musical",
      "Teen"
    ]
  }
]


def insert_data(user_data, title_data):
    title_ids = []
    for title in title_data:
        title['uploadDate'] = random_date()
        title['dateReleased'] = random_date()
        title_id = create_title(title)
        title_ids.append(title_id)
    # Test creating a user
    for user in user_data:
        user_id = create_user(user)

        login_data = create_login_data(user_id, True)
        create_login_log(login_data)
        
        for i in range(random.randint(1, 3)):
            title_id = random.choice(title_ids)
            watch_history_data = create_watch_history_data(user_id, title_id, random.randint(0,240))
            create_watch_history(watch_history_data)

            # Test creating an event log
            event_data = create_event_data(user_id, "login", "User logged in successfully")
            create_event(event_data)

            rating_data = create_rating_data(user_id, title_id, random.randint(0, 5), comment="great movie!")
            create_rating(rating_data)



    
def main():
    insert_data(user_data, title_data)

if __name__ == "__main__":
    main()
