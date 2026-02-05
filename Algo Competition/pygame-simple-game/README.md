# pygame-simple-game

## Overview
This is a simple game built using Pygame. The game features a main menu, gameplay mechanics, and a heads-up display (HUD) to show important information to the player.

## Project Structure
```
pygame-simple-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game.py          # Main game class managing game state
│   ├── settings.py      # Game settings and configurations
│   ├── scenes           # Contains different game scenes
│   │   ├── __init__.py  # Initializes the scenes package
│   │   ├── menu.py      # Main menu scene
│   │   └── play.py      # Gameplay scene
│   ├── entities         # Contains game entities
│   │   ├── __init__.py  # Initializes the entities package
│   │   ├── player.py     # Player character class
│   │   └── enemy.py      # Enemy character class
│   ├── ui               # Contains UI elements
│   │   └── hud.py       # HUD class for displaying game info
│   ├── assets           # Game assets like fonts and audio
│   │   ├── fonts        # Font files used in the game
│   │   │   └── README.md # Information about fonts
│   │   └── audio        # Audio files used in the game
│   │       └── README.md # Information about audio assets
│   └── utils            # Utility functions
│       └── helpers.py   # Helper functions for various tasks
├── tests                # Unit tests for the game
│   └── test_game.py     # Tests for game logic
├── requirements.txt     # Project dependencies
├── pyproject.toml       # Project configuration
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd pygame-simple-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game
To start the game, run the following command:
```
python src/main.py
```

## Gameplay
- Use the menu to start the game or exit.
- During gameplay, control the player character and interact with enemies.
- The HUD displays your score and health.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.