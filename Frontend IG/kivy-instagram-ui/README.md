# Kivy Instagram UI

This project is a Kivy-based application that mimics the frontend interface of Instagram. It is designed to provide a user-friendly experience for browsing posts, viewing profiles, and exploring content without a backend.

## Project Structure

```
kivy-instagram-ui
├── src
│   ├── main.py                # Entry point of the application
│   ├── app.py                 # Main application class managing screens
│   ├── screens                # Contains different screen classes
│   │   ├── home_screen.py     # Home screen displaying the feed
│   │   ├── profile_screen.py  # User profile screen
│   │   ├── explore_screen.py  # Explore screen for discovering content
│   │   └── post_detail_screen.py # Detailed view of a specific post
│   ├── widgets                # Custom widgets for the app
│   │   ├── post_card.py       # Widget for displaying individual posts
│   │   ├── story_widget.py     # Widget for displaying user stories
│   │   └── nav_bar.py        # Navigation bar widget
│   ├── kv                     # Kivy language files for UI layouts
│   │   ├── main.kv           # Main layout definitions
│   │   ├── home.kv           # Home screen layout definitions
│   │   ├── profile.kv        # Profile screen layout definitions
│   │   └── widgets.kv        # Custom widget layout definitions
│   ├── data                   # Mock data for the app
│   │   └── mock_data.py       # Sample posts and user information
│   └── assets                 # Assets for the app
│       ├── icons              # Icon files
│       └── fonts              # Font files
├── tests                      # Unit tests for the application
│   └── test_ui.py            # Tests for UI components
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files to ignore in version control
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kivy-instagram-ui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- Navigate through the app using the navigation bar at the bottom.
- View the home feed, explore new content, and check user profiles.
- The app is designed to be a static frontend without backend functionality.

## Contributing

Feel free to submit issues or pull requests for improvements or features.