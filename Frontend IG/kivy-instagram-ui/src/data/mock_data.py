# filepath: kivy-instagram-ui/src/data/mock_data.py

mock_posts = [
    {
        "id": 1,
        "username": "user1",
        "image": "assets/images/post1.jpg",
        "caption": "Loving the sunset!",
        "likes": 120,
        "comments": [
            {"username": "user2", "text": "Beautiful!"},
            {"username": "user3", "text": "Wish I was there!"}
        ]
    },
    {
        "id": 2,
        "username": "user2",
        "image": "assets/images/post2.jpg",
        "caption": "Just another day at the beach.",
        "likes": 95,
        "comments": [
            {"username": "user1", "text": "Looks fun!"},
            {"username": "user4", "text": "I love the beach!"}
        ]
    },
    {
        "id": 3,
        "username": "user3",
        "image": "assets/images/post3.jpg",
        "caption": "Exploring the mountains.",
        "likes": 150,
        "comments": [
            {"username": "user1", "text": "Amazing view!"},
            {"username": "user2", "text": "Nature is beautiful!"}
        ]
    }
]

mock_users = [
    {
        "username": "user1",
        "full_name": "User One",
        "profile_picture": "assets/images/user1.jpg",
        "bio": "Adventure seeker and photographer."
    },
    {
        "username": "user2",
        "full_name": "User Two",
        "profile_picture": "assets/images/user2.jpg",
        "bio": "Beach lover and travel enthusiast."
    },
    {
        "username": "user3",
        "full_name": "User Three",
        "profile_picture": "assets/images/user3.jpg",
        "bio": "Mountain climber and nature lover."
    }
]