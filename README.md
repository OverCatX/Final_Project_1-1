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
| Title            | Description                                                                                          | Duration (seconds) |
|------------------|------------------------------------------------------------------------------------------------------|--------------------|
| **x2 Score**     | Doubles the score for all points earned during the event duration.                                   | 10                 |
| **Slowed Ball**  | Reduces the speed of the ball(s), making it easier to control gameplay.                              | 10                 |
| **Big Paddle**   | Temporarily increases the size of the paddle for better control and easier ball deflection.          | 5                  |
| **Save Ball**    | Automatically prevents the ball from falling off once during the event duration.                     | 10                 |
| **x3 Score**     | Triples the score for all points earned during the event duration.                                   | 6                  |
| **Balls x2**     | Introduces an additional ball into gameplay, increasing the difficulty.                              | -                  |
| **Balls x3**     | Introduces two additional balls into gameplay, significantly increasing the challenge.               | -                  |

**How Events Work:**
- **Activation:** Events are triggered based on game mechanics (e.g., power-ups or random timers).
- **Duration:** Each event lasts for a limited time as specified in the table.
- **Stacking:** Some events, like Balls x2 and Balls x3, stack and can create chaotic and challenging gameplay.


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
- **Increased Collision Handling**
  - **Challenge:** Multiple balls increase the likelihood of simultaneous collisions between balls and paddles or between balls themselves.
  - **Mechanics:**
    - Ensure your collision detection can handle multiple objects efficiently.
    - Prevent “chain reaction” bugs (e.g., one collision causing incorrect or infinite responses in others).
    - Resolve overlaps to avoid balls getting stuck inside each other.
- **Enhanced Ball Dynamics**
  - **Challenge:** Tracking and updating the movement of multiple balls in real time.
  - **Mechanics:**
    - Use a loop to update the position and velocity of each ball during every frame.
    - Maintain consistent ball speeds, applying friction or capping velocities to prevent runaway speeds.
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
      - The PadBallGame class is a comprehensive implementation of a state-driven arcade game built. It manages the entire flow of the game, including the user interface, state transitions, gameplay mechanics, and interaction with the leaderboard database. This class is responsible for rendering different game screens, handling user inputs, updating game objects, and enforcing rules and conditions during gameplay. 
      - **Key Attributes:**
        - Screen Setup and Display
          - screen_width: width of the game window in pixels (600).
          - screen_height: height of the game window in pixels (800).
          - screen: A pygame.Surface object representing the game window, created using pygame.display.set_mode().
          - clock: A pygame.time.Clock instance used to control the frame rate of the game.
        - Audio
          - sound: An instance of the Sound class that handles game sound effects and background music.
        - Game State and Data
          - running: A boolean indicating whether the game is running.
          - game_data: A dictionary that tracks the game’s state, settings, and events, including:A dictionary that tracks the game’s state, settings, and events, including:
            - username: The player’s username.
            - state: Current game screen (e.g., “home,” “play”).
            - scores: Player’s current score.
            - ball_speed_origin: Base speed of the ball.
            - event_status: Indicates whether a special event is active.
            - event_id: Tracks the active event by ID (e.g., “#001” for x2 Score).
          - events:
            - A dictionary mapping event IDs (e.g., #001) to their properties (title and duration).
        - Game Entities
          - floating_balls: A list of FloatingObject instances with random properties (e.g., size, velocity, position).
          - ball_game: A Ball instance representing the main ball of the game.
          - mystery_box: A MysteryBlock instance representing a special item that appears during the game.
          - paddle: A Paddle instance representing the player’s paddle.
          - wood_paddle: A secondary Paddle instance used for specific events (e.g., expanded paddle).
          - save_ball_paddle: A Paddle instance acting as a safety net to save the ball under certain conditions.
        - Fonts and Visual Elements
          - fonts: A dictionary of pygame.font.Font objects, categorized by size (Large, Medium, Small) for rendering text on different screens.
          - buttons: A dictionary of Button instances, each representing a button for game navigation (e.g., “Start Game,” “Leaderboard”).
          - color_codes: A dictionary of common color names mapped to RGB tuples for easy reference in the game’s visual elements.
      - **Key Methods:**
        - turn_default_data: 
          - A method resets the game state and reinitializes all game entities to their default configurations. It sets default values for scores, ball speed, event states, and screen color. Additionally, it regenerates floating objects, the main ball, and paddles with their initial properties, ensuring a fresh start for a new game or after a reset.
        - authorization_screen:
          - Displays a screen where players can enter a username.
            - Accepts input using the keyboard (backspace to delete, enter to confirm).
            - Validates the username length (maximum of 15 characters).
            - Contains buttons to proceed to the next state (lobby) or return to the home screen.
        - home_screen:
          - Serves as the main menu screen for the game.
            - Displays floating balls for a dynamic visual effect.
            - Includes buttons for starting the game, viewing the leaderboard, viewing reports, or exiting.
            - Handles user interactions for these buttons to transition between states.
        - lobby_screen:
          - Displays a welcome screen personalized with the player’s username.
            - Contains floating ball animations for visual appeal.
            - Prepares the player to transition to gameplay or other game states.
        - on_game
          - Represents the core gameplay loop.
            - Resets game data and initializes the gameplay environment.
            - Tracks player scores, manages events (e.g., mystery box bonuses), and updates visuals like paddles, balls, and score text.
            - Handles collision detection and bonus events:
              - Mystery box spawns randomly when the score exceeds a threshold.
              - Various bonus effects (e.g., slowed ball, larger paddle, etc.) are triggered upon hitting the box.
            - Checks for game-over conditions and updates the score.
            - Allows paddle control via keyboard (left/right arrows).
        - game_over
          - Displays the game-over screen after losing.
            - Shows the player’s score and best score.
            - Provides buttons for restarting the game or returning to the home screen.
        - leaderboard
          - Displays the leaderboard with the top 10 players, fetched from the database.
            - Highlights the current player if they are on the leaderboard.
            - Includes a back button to return to the home screen.
        - run
          - The main game loop.
            - Continuously checks the current game state (game_data['state']) and calls the corresponding screen method.
            - Ensures the game flow is seamless between different states.
            - Handles the exit condition by quitting the game when self.running is False.
      - **Highlights:**
        - **Dynamic Gameplay**:
          - The on_game method dynamically adjusts gameplay based on events, such as bonuses for hitting the mystery box.
        - **User Interactions:**
          - Supports keyboard and mouse inputs for controlling gameplay and navigating menus.
        - **State Management:**
          - Uses game_data['state'] to determine which screen to display and transitions smoothly between states.
        - **Visuals and Effects:**
          - Includes floating balls, paddle animations, and text rendering for an engaging user experience.
        - **Persistence:**
          - Uses a database (PlayerDB) to fetch leaderboard data and save player scores.
      - **General Flow:**
        1. The game starts in the home screen.
        2. The player can navigate to the authorization screen to enter their username.
        3. Upon successful login, the game transitions to the lobby screen.
        4. From the lobby, the player starts the gameplay (on_game), where scores are tracked, and events can occur.
        5. The game ends in the game_over screen, with options to restart or return to the main menu.
        6. Players can also view the leaderboard from the home screen.
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
        - on_hit_balls(balls):
          - This method checks if the ball (calling the method) collides with any of the other balls in the balls list, and if a collision is detected, it adjusts the ball’s position and velocity accordingly. It returns True if a collision occurred and False if no collision was detected.
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
                player = db.player_login('Bhumipat')
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
  - The `ball_bouncing_sim_oo`based `Ball` class served as the foundation for the design of the **FloatingObject** and **Ball** classes in **PadBallGame**. The transition involved adapting the simulation logic from a Turtle graphics system to Pygame’s event-driven framework, while also incorporating additional features to enhance flexibility and interactivity, including **event bonuses** that increase the number of balls on screen (e.g., **Ball x2** and **Ball x3** events). Below are the key aspects of this modification process:
  - **Decoupling Generic Behavior (FloatingObject)**
    - **Purpose of Change**:  
      - The **FloatingObject** class was introduced as a general-purpose base class to represent any floating entity (not limited to balls). This abstraction allows for easier extension of functionality and reuse in various game elements.
    - **Key Modifications**:
      - **Abstracted common properties** like size, position (x, y), velocity (vx, vy), color, and screen boundaries.
      - **Simplified edge-collision detection** and response for generic floating objects.
      - **Added functionality** to manage multiple instances of **Ball** objects, as the game can spawn additional balls during special events (e.g., Ball x2, Ball x3).
      - **Support for new behavior** introduced by event bonuses that spawn extra balls, ensuring that their interactions (collisions with other balls) are handled efficiently.

  - **Specializing Behavior (Ball class)**
     - The **Ball class** builds on **FloatingObject**, integrating specialized logic for game-specific interactions, such as bouncing off paddles, mystery boxes, and sound effects.
     - **Key Modifications Based on `ball_bouncing_sim_oo`:**
       - **Collision Handling**:
         - Extended the **collision handling** to accommodate new game mechanics introduced by **event bonuses** like **Ball x2** and **Ball x3**.
         - Implemented **ball-to-ball collision detection** to ensure that when new balls are spawned during these events, they interact with existing balls correctly.
         - Kept the **physics-based collision logic** (e.g., bouncing off walls and objects) but adapted it for the Pygame event loop.
         - Enhanced **paddle-specific collision handling** to manage edge cases (e.g., hitting paddle corners).
   
       - **Interactions with New Elements**:
         - Modified methods to detect **collisions with new balls** spawned during event bonuses.
         - The **ball-to-ball collision logic** was added, allowing newly spawned balls (from events like Ball x2 and Ball x3) to interact dynamically with each other.
   
       - **Event Loop Compatibility**:
         - Integrated the **event bonuses** into the main event loop, triggering the spawning of additional balls when the events are active.
         - Added **event duration management** to ensure that new balls are removed after the event ends.

  - **Sound Effects**:
     - Incorporated Pygame’s sound functionality to enhance feedback during **collisions**, including those between multiple balls. 
     - **Event-triggered sound effects** were introduced to notify players when the **Ball x2** or **Ball x3** events occur, adding more immersion to the gameplay experience.

  - **Physics Adaptation**:
    - While the **ball_bouncing_sim_oo** Ball relied on explicit calculations for collision timing and response, the **PadBallGame** Ball class simplifies this by integrating with **frame-based updates**, enabling **real-time responsiveness**. This trade-off balances realism and performance for interactive gameplay.
    - With **Ball x2** and **Ball x3** events, the game now manages multiple balls at once, adjusting **velocity**, **collision detection**, and **event handling** to ensure smooth and continuous gameplay.

  - **Event Bonuses and Ball Collisions:**
    - **Ball x2**: Doubles the number of balls in the game for a short period. When this event occurs, two new balls are spawned and added to the game’s ball list. These balls will interact with existing balls, and collision handling has been extended to accommodate this.
    - **Ball x3**: Triples the number of balls on screen during its duration. Similar to **Ball x2**, the game spawns three new balls that interact with each other and the existing balls. Collisions between all balls are now handled dynamically by the `on_hit_balls()` method, which has been enhanced to account for this increase in objects on screen.
    
- **Conclusion:**
  - The modifications made to the **PadBallGame** framework involve adapting the **ball_bouncing_sim_oo** `Ball` class to fit within a more interactive, event-driven system. By incorporating event bonuses like **Ball x2** and **Ball x3**, and expanding the **FloatingObject** and **Ball** classes to handle multiple balls, the game’s complexity and playability are enhanced. These changes introduce dynamic new challenges for players, making the game more engaging and exciting.
  - This project only use Pygame library for draw any shape,screen interface and add sound on background screen or sound effect when ball hit paddle or wall etc

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
Watch the Project demonstration here: [PadballGame Demo Video](https://www.youtube.com/channel/UC-nrlXpjGtabRQYM1y010xA)

## Submission
- **GitHub Repository:** [PadballGame Repository](https://github.com/OverCatX/PadballGame-V.1/tree/main)
- **Demo Video:** [PadballGame Demo Video](https://www.youtube.com/channel/UC-nrlXpjGtabRQYM1y010xA)

Enjoy playing PadballGame ><