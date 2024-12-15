# Padball: The Ultimate Paddle-Bouncing Game

## Description

Padball is an engaging and fast-paced game that combines skill, strategy, and reflexes. The player controls a paddle to bounce a ball, aiming to hit randomly appearing mystery boxes and score points while avoiding the ball falling off the screen. As the game progresses, various bonus events, such as double points, slow ball, and paddle transformations, triple points, save ball paddle, add an exciting layer of complexity to challenge and entertain the player.

## Features
### Gameplay Elements:
- **Player-Controlled Paddle:**
    - The paddle is the primary tool the player uses to bounce the ball.
    - Players must skillfully move the paddle left and right to keep the ball in play and when your scores more than 2 there will have MysteryBox-Bonus appear you can aim for targets like the mystery boxes to get a good random bonus.
- **Bouncing Ball Mechanic:**
    - The ball moves dynamically and reacts to collisions with the paddle and other elements in the game.
    - The challenge lies in timing and positioning the paddle correctly to keep the ball bouncing and in play.
- **Mystery Boxes:**
    - Mystery boxes appear at random positions on the screen.
    - Mystery boxes appear when player scores more than 2.
    - The player aims to hit these boxes with the ball to trigger special events or score points.
    - Adds a layer of strategy as the player decides whether to focus on mystery boxes or simply keep the ball in play.

### Bonus Events:
- **Double Points:**
    - 10 seconds bonus to double the points scored.
    - Encourages the player to aim for high-scoring plays while the bonus is active.
- **Triple Points:**
    - 6 seconds bonus to triple the points scored.
    - Increases the excitement as players strive for their best moves during this period.
- **Slow Ball:**
    - 10 seconds momentarily slows down the ball for precise control.
    - A helpful event for players when the game becomes fast-paced and challenging.
- **Paddle Transformations:**
    - 5 seconds change paddle size or shape for additional challenges.
    - For instance, a full-width paddle makes it easier to keep the ball in play but may also require faster reflexes due to increased collision frequency.
- **Save Ball Paddle:**
    - Adds a safety net for 10 seconds.
    - This paddle automatically saves the ball if it falls, preventing immediate game over and giving the player another chance to score.

### Leaderboard System:
- Compete for the top score with other players.
- Scores are sorted in descending order to showcase the best-performing players at the top.
- The game tracks the top 10 scores, encouraging players to compete for the highest rankings.
- Players can enter their name to personalize their high score when they achieve a new record.
- The leaderboard updates automatically as players complete games and score points, reflecting the latest high scores in real-time.
- By showcasing the top scores, the leaderboard motivates players to keep playing to beat their previous records or outperform others.
- Automatically records and displays the top 10 best scores after every game.
- Saves best scores locally, ensuring your progress is never lost.

### Progressive Difficulty:
- The game introduces faster ball speeds and fewer bonuses over time.

### Advanced Mechanics:
- **Randomized Elements:**
  - Mystery boxes and bonus events are randomized, ensuring that each game feels unique and keeps the player engaged.
- **Difficulty Scaling:**
  - As the game progresses, the ball may speed up or require more precision to keep the player on their toes.

### Player Objectives
- **Score Points:**
  - The primary goal is to score as many points as possible by hitting mystery boxes and keeping the ball in play.
  - Competing with others or their past performances adds a layer of excitement and replayability.
- **Climb the Leaderboard:**
  - Players aim to achieve a score high enough to appear in the Top 10.
  - Competing with others or their past performances adds a layer of excitement and replayability.
- **Survive:**
  - Avoid letting the ball fall off the screen, which ends the game.
  - Use skill, reflexes, and bonus events like the save ball paddle to extend gameplay.

## How to Install and Run the Project
1. Clone the Repository:
    ```shell 
   git clone https://github.com/OverCatX/PadballGame-V.1.git
   ```
   If you finished cloning the repository then
   ```shell
   cd PadballGame-V.1
   ```
2. Install Dependencies:\
    <sub>Ensure you have Python 3.10+ installed.</sub>
    ```shell
    python --version
    ```
3. Install Pygame:\
    <sub>Use pip to install Pygame, which is required for this project.</sub>
    ``` shell
    pip install pygame
    ```
4. Run Game:\
    <sub>Execute the main file to start the game:</sub>
    ``` shell
    python padball_game.py
    ```

## How to Control
- Use the Left Arrow Key (←) to move the paddle to the left.
- Use the Right Arrow Key (→) to move the paddle to the right.
- Your goal is to bounce the ball back into play and hit mystery boxes to score points.

## Usage:
- Game Controls:
    - Use the arrow keys to move the paddle left or right.
    - Bounce the ball to hit mystery boxes and activate bonuses.
- Gameplay Example:
    - Start the game and control the paddle to keep the ball in play.
    - A mystery box appears when your score more than 2 at random position; hit it to activate a bonus events.
    - Avoid letting the ball fall off the screen.
- Leaderboard:
    - After each game, your score is compared to previous high scores.
    - The leaderboard displays the top 10 best scores player along with player names or initials.
- Expected Outputs:
    - Real-time score updates as you hit mystery boxes or activate bonuses.

For a detailed walkthrough of the gameplay, watch the [demo video.](https://github.com/OverCatX/PadballGame-V.1/tree/main?tab=readme-ov-file#demo-video)

## Project Design and Implementation

- ### UML Class
![UmlClass](https://github.com/OverCatX/PadballGame-V.1/blob/main/PadBallGame-UML.jpeg?raw=true)

- ### Class Descriptions:
    - **PadBallGame:** 
    - **FloatingObject:** 
      - The FloatingObject class serves as a base class for objects that have movement behavior within a bounded 2D space (such as the screen). It provides shared functionality for updating position, detecting screen-edge collisions, and rendering itself on the screen.
      - **Key Attributes:**
        - size: Radius of the floating object (circle).
        - x, y: Current position of the object on the screen.
        - vx, vy: Velocity of the object in the x and y directions.
        - color: Color of the object, represented as an RGB tuple.
        - screen_width, screen_height: Dimensions of the screen for boundary checks.
        - sound: A Sound object to handle audio feedback for collisions.
      - **Key Methods:**
        - __init__: Initializes the object’s size, position, velocity, color, and screen boundaries.
        - draw(display): Draws the object on the provided display surface as a circle.
        - updates(): Updates the object’s position based on its velocity and checks for collisions with the screen edges.
        - on_hit_screen_edge(): Detects if the object has collided with the screen edges. If so, it reverses the velocity in the respective direction to simulate a bounce.
    - **Ball:**
      - The Ball class extends the FloatingObject class to represent the primary interactive object in the game. It inherits all the functionality of FloatingObject but adds logic for interacting with game elements such as paddles, mystery boxes, and save-ball paddles.
      - **Key Attributes:**
        - Inherits all attributes from FloatingObject.
      - **Key Methods:**
        - __init__: Calls the parent class constructor and initializes a Ball object with default or user-provided attributes (size, position, velocity, color, etc.).
        - updates(paddle=None, wood_paddle=None, mystery_box=None, box_active=False, save_ball_paddle=None, save_ball_active=False):
          - Overrides the parent updates method to include logic for interacting with various game elements:
            - Detects and handles collisions with paddles.
            - Interacts with mystery boxes when they are active.
            - Accounts for “save-ball” paddles.
        - on_hit_screen_edge():
          - Extends the parent method by adding sound effects when the ball collides with screen edges.
        - on_hit_paddle(paddle):
          - Detects collisions with a standard paddle.
          - Adjusts the ball’s velocity depending on which side of the paddle (top, bottom, left, or right) it hits.
        - on_hit_wood_paddle(paddle):
          - Similar to on_hit_paddle, but used for collisions with a “wood paddle” (potentially a special paddle type).
        - on_hit_save_paddle(paddle, save_ball_active):
          - Handles collisions with a special “save-ball paddle” when the save-ball feature is active.
        - on_hit_mystery_box(box, box_active):
          - Checks for collisions with a mystery box if it is active. If the ball collides with the box, the method returns True.
        - __str__():
          - Returns the string representation of the ball object as 'ball'.
      - **How These Classes Interact:**
        - FloatingObject provides shared functionality:
          - Basic physics (movement and bouncing off edges).
          - Rendering functionality for objects represented as circles.
          - Acts as a reusable base for any floating object in the game.
        - Ball extends FloatingObject with game-specific logic:
          - Interacts with paddles, mystery boxes, and save-ball paddles.
          - Provides specialized behavior for different types of objects, making it integral to the gameplay.
        - These two classes showcase modular design, with FloatingObject encapsulating generic behavior and Ball adding game-specific logic. This approach promotes code reusability and easy maintenance.
    - **MysteryBox:**
      - The MysteryBlock class represents a rectangular block that can appear on the screen as part of the game. It is designed to serve as an interactive element that players aim to hit with the ball to trigger various game events or bonuses.
      - **Key Attributes:**
        - width: Determines the horizontal size of the rectangle on the screen.
        - height: Determines the vertical size of the rectangle on the screen.
        - x,y: x defines the horizontal position, and y defines the vertical position.
        - color: The color of the mystery block, specified as an RGB tuple (e.g., (255, 0, 0) for red).
        - screen_width: The width of the screen (defaulted to 800).
        - screen_height: The height of the screen (defaulted to 600).
      - **Key Methods:**
        - __init__(self, width, height, x, y, color)
          - The constructor initializes the mystery block’s dimensions (width and height), position (x, y), and its color.
          - It also sets the screen boundaries for reference purposes.
        - draw(self, display)
          - Uses the pygame.draw.rect() function to draw the mystery block as a rectangle on the given display surface.
          - The block is filled with the color specified during initialization.
      - **Role in the Game:**
        - When the ball collides with the block, the game can trigger bonuses or special events, such as extra points, temporary ball effects (e.g., slowing the ball), or paddle transformations.
    - **Paddle**
      - The Paddle class represents a paddle in the game, controlled by the player to interact with the ball. It is designed to serve as the primary tool for keeping the ball in play and directing it toward mystery blocks or other targets.
      - **Key Attributes:**
        - width: The width of the paddle (in pixels).
        - height: The height of the paddle (in pixels).
        - x, y: The position of the top-left corner of the paddle.
        - color: The color of the paddle, defined as an RGB tuple (e.g., (0, 0, 255) for blue).
        - speed: The speed at which the paddle can move (in pixels per update).
      - **Key Methods:**
        - __init__(self, width, height, x, y, color, speed)
          - Ensures that the paddle is ready for drawing and interaction in the game.
        - draw(self, display)
          - Draws the paddle on the game screen using pygame.draw.rect().
        - __str__(self)
          - Returns a string representation of the paddle object ("paddle").
      - **Role in the Game:**
        - The Paddle class is a core gameplay element that allows the player to control the ball’s trajectory.
        - The paddle serves as both a defensive tool (preventing the ball from falling) and an offensive tool (directing the ball toward mystery blocks or targets).
        - The player moves the paddle horizontally (or vertically, depending on game design) to bounce the ball back into play.
    - **PlayerDB:**
      - PlayerDB is a class for managing the game’s player database, including creating records, checking user existence, updating high scores, and retrieving the leaderboard.
      - **Key Attributes:**
        - players_db: A string representing the path to the database file (players.csv).
          - Default value is db/players.csv.
        - data: A list for temporarily storing player records during updates.
      - **Key Methods:**
        - __init__(self, db_file=database_file)
          - Initializes the database path.
          - If the file doesn’t exist, creates it with the headers ['Username', 'HighScore'].
        - player_exists(self, username) -> bool
          - Checks if a player exists in the database by their username.
          - Compares usernames in a case-insensitive manner.
            - **Return**
              - True: If the player is found.
              - False: Otherwise.
        - player_login(self, username)
          - Logs in a player by checking if they exist.
            - If not: Adds a new record for the username with a score of 0 and returns a Player object.
            - If found: Returns a Player object initialized with the username and high score.
        - set_new_highscore(self, username, highscore)
          - Updates a player’s high score in the database.
          - Reads all data, modifies the matching record, and rewrites the database.
        - get_leaderboard(self)
          - Retrieves all player records and sorts them by HighScore in descending order.
          - Returns: A list of player records sorted by high scores.
      - **Role in the Game**
        - PlayerDB acts as the backend system for maintaining player data.
        - Ensures persistent storage of player usernames and high scores.
        - Facilitates features like player login, high-score updates, and leaderboard generation.
    - **Player**
      - Player represents an individual player with attributes like username and high score. It interacts with the PlayerDB class to manage high-score updates.
      - **Key Attributes:**
        - username: A string representing the player’s username.
        - highscore: An integer representing the player’s highest score.
      - **Key Methods:**
        - __init__(self, username: str, highscore: int)
          - Initializes a player with their username and high score.
        - updates_best_score(self, score)
          - Updates the player’s high score to a new value (score).
          - Calls PlayerDB().set_new_highscore to update the database.
          - Prints a message confirming the update.
        - __str__(self)
          - Returns a string representation of the player object in the format:
            - Player: {username}, HighScore: {highscore}.
      - **Role in the Game**
        - Represents the user’s profile, keeping track of their personal high score.
        - Provides a simple interface to update scores and interact with the database.
      - **Relationship Between PlayerDB and Player**
        - PlayerDB serves as the database manager, handling all player-related data in the system.
        - Player represents individual users and utilizes PlayerDB for persistence and updates.
        - Together, these classes enable a seamless experience for managing players, updating high scores, and displaying leaderboards.
          - Usage Example
            - Login a Player
                ``` shell
                db = PlayerDB()
                player = db.player_login('john_doe')
                print(player)
                ```
            - Update High Score
                ``` shell
                player.updates_best_score(150)
                ```
            - Display Leaderboard
                ``` shell
                leaderboard = db.get_leaderboard()
                for player in leaderboard:
                    print(player)
                ```
    - **Sound**
      - The Sound class manages the audio features of the game, including background music and sound effects for specific game events. It uses the pygame.mixer module to load, play, and control audio.
      - **Key Attributes:**
        - hit_wall_sound: A pygame.mixer.Sound object for the sound effect played when the ball hits a wall.
        - hit_paddle_sound: A pygame.mixer.Sound object for the sound effect played when the ball hits a paddle.
        - background_sound: A pygame.mixer.Sound object for the background music of the game.
      - **Key Methods:**
        - __init__(self)
          - Initializes the sound objects by loading the corresponding audio files for wall hit, paddle hit, and background music.
        - run_background_sound(self)
          - Plays the background music in a continuous loop (-1).
        - run_sound(self, sound)
          - Plays a specific sound effect based on the provided string input:
            - 'wall': Plays the wall hit sound (hit_wall_sound).
            - 'paddle': Plays the paddle hit sound (hit_paddle_sound).
        - stop_wall_sound(self)
          - Stops the wall hit sound (hit_wall_sound) immediately.
      - **Role in the Game**
        - The Sound class enriches the game by adding an auditory layer that enhances the player’s experience.
        - Background Sound: Keeps the game engaging with continuous music.
        - Event-Specific Sounds: Provides feedback for in-game actions like hitting a paddle or wall.
    - **Button**
      - The Button class represents a clickable button in a game or application interface. It handles rendering the button on the screen and detecting user interactions, such as mouse clicks.
      - **Key Attributes:**
        - rect: A pygame.Rect object that defines the button’s position (x, y), width, and height.
        - text: A string representing the text displayed on the button.
        - text_color: A tuple (R, G, B) representing the color of the button’s text.
        - button_color: A tuple (R, G, B) representing the color of the button itself.
        - font: A pygame.font.Font object defining the font and size of the button’s text.
      - **Key Methods:**
        - __init__(self, x, y, width, height, text, text_color, button_color)
          - Creates a rectangular area for the button (rect) and prepares the text font.
        - draw(self, display)
          - Draws the button rectangle using its color and adds the centered text on top.
        - is_clicked(self, mouse_pos)
          - Checks if the button is clicked by detecting if the mouse position is within the button’s rectangular area.
      - **Role in the Game**
        - Interface Element: Provides a way for players or users to interact with the game, such as starting a game, pausing, or accessing settings.
        - Event Handling: Detects and responds to user clicks for interactive functionality.

## Code Implementation Details
- **Baseline Code Modifications:**
  - Extend
- **Leaderboard System:**
  - implement

## Testing and Known Issues:
- **Testing:**
  - Conducted multiple gameplay tests to ensure all features work as intended
  - Verified bonus event triggers scoring mechanics, and leaderboard updates
- **Known Bugs:**
  - Occasionally, rapid ball-paddle collisions may not go in direction correctly in high-speed(vx,vy > 20) modes.

## Project Sophistication Level
**Rating: 90**
- Reason: Includes dynamic gameplay with multiple event-driven mechanics and object interactions. Features bonus events, a leaderboard system, and progressive difficulty, making it more advanced than basic pong games but not as complex as multi-object simulations like snooker.

## Demo Video
Watch the Project demonstration here: [Padball Demo Video](https://www.youtube.com/channel/UC-nrlXpjGtabRQYM1y010xA)

## Submission
- **GitHub Repository:** [Padball Repository]()
- **Demo Video:** [Padball Demo Video]()

Enjoy playing PadballGame ><