# Padball: The Ultimate Paddle-Bouncing Game

## Description

Padball is an engaging and fast-paced game that combines skill, strategy, and reflexes. The player controls a paddle to bounce a ball, aiming to hit randomly appearing mystery boxes and score points while avoiding the ball falling off the screen. As the game progresses, various bonus events, such as double points, slow ball, and paddle transformations, triple points, save ball paddle, add an exciting layer of complexity to challenge and entertain the player.

## Features
### Gameplay Elements:
- Player-Controlled Paddle:
    - The paddle is the primary tool the player uses to bounce the ball.
    - Players must skillfully move the paddle left and right to keep the ball in play and when your scores more than 2 there will have MysteryBox-Bonus appear you can aim for targets like the mystery boxes to get a good random bonus.
- Bouncing Ball Mechanic:
    - The ball moves dynamically and reacts to collisions with the paddle and other elements in the game.
    - The challenge lies in timing and positioning the paddle correctly to keep the ball bouncing and in play.
- Mystery Boxes:
    - Mystery boxes appear at random positions on the screen.
    - Mystery boxes appear when player scores more than 2.
    - The player aims to hit these boxes with the ball to trigger special events or score points.
    - Adds a layer of strategy as the player decides whether to focus on mystery boxes or simply keep the ball in play.

### Bonus Events:
- Double Points:
    - 5 seconds bonus to double the points scored.
- Triple Points:
    - 5 seconds bonus to triple the points scored.
- Slow Ball:
    - 10 seconds momentarily slows down the ball for precise control. 
- Paddle Transformations:
    - 5 seconds change paddle size or shape for additional challenges.
- Save Ball Paddle:
    - Adds a safety net for 5 seconds.

### Leaderboard System:
- Compete for the top score with other players.
- Automatically records and displays the top 10 best scores after every game.
- Saves best scores locally, ensuring your progress is never lost.

### Progressive Difficulty:
- The game introduces faster ball speeds and fewer bonuses over time.

### Friendly-Controls:
- Intuitive controls suitable

## How to Install and Run the Project
**1. Clone the Repository:**
    ```shell 
   git clone https://github.com/OverCatX/PadballGame-V.1.git
   ```
   If you finished cloning the repository then
   ```shell
   cd PadballGame-V.1
   ```
**2. Install Dependencies:\**
    Ensure you have Python 3.10+ installed.
    ```shell
    python --version
    ```
**3. Run Game:\**
    Execute the main file to start the game:
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

## Project Sophistication Level
**Rating: 90**
- Reason: Includes dynamic gameplay with multiple event-driven mechanics and object interactions. Features bonus events, a leaderboard system, and progressive difficulty, making it more advanced than basic pong games but not as complex as multi-object simulations like snooker.
