==> Turtle Crossing Game (OOP – Python)
 
* Turtle Crossing Game is an object-oriented game built with Python’s turtle module.
* The player controls a turtle that must cross a busy road while avoiding randomly generated cars. Each successful crossing increases the difficulty by speeding up the traffic.

This project focuses on:

* Object-Oriented Programming (OOP) that I considere it for practicing it
* Game loops and collision detection, which help us to practice basic python like loops and conditions
* Clean separation of responsibilities between classes, in order to practice my logic of programming

=> The steps to the end of project:
 What things I do the certain path is the in the below:
 1. Having an overview and making a plan and checklist up to the end of the project.
 2. The plan:
     1. Turtle crossing:
        screen, field
        starting position
        sitting steps
        finishing line
        moving turtle
        expressing the onkey on the screen
     2. Making the cars:
        set the starting position
        creating in random y posiotion
        moving the cars, looping throught the cars list
        detecting if the player reach the final line 
     4. Game over logic:
        detecting the collision with cars
     5. Score:
        creating the score and showing it
        tracking score
        adding score
        updating the scores
 3. Editing
    
=> Gameplay

* Press SPACE to move the turtle forward
* Avoid cars if you collid the cars, you will lose and the game is over
* Reach the top of the screen to pass the current mission and go to the next level
* Each level increases car speed

=> Project Structure
turtle_crossing_game
:
** main.py          # Main game loop and screen setup
** player.py        # Player (turtle) behavior
** cars.py          # Car generation and movement logic
** score.py         # Level display and game-over message
** README.md        # Offer the documentation for the turtle crossing game

=> Class Responsibilities:

* Player (inherits from Turtle)
  Handles player movement and level reset logic.
Key features:
  Starts at the bottom of the screen
  Moves upward in fixed steps
  Resets position when a level is completed
Main methods:
  move() – Moves the player forward
  new_level() – Resets player position after success

* cars
  Controls all car-related behavior.
Key features:
  Random car generation
  Horizontal movement across the screen
  Progressive speed increase per level
Main methods:
  create_car() – Randomly creates cars
  move_cars() – Moves all cars left
  speed_up() – Increases car speed after each level

* Score
  Manages level display and game-over message.
Key features:
  Displays current mission (level)
  Updates level count
  Shows “Game Over” on collision
Main methods:
  update_level() – Increases and redraws level
  game_over() – Displays game over message

=> How the while loop works:

Screen updates every 0.1 seconds
Cars may randomly spawn
Cars move left each frame
Player position is checked:
Reaches top → next level
Collides with car → game over

=> Requirements
* Python 3.8+
* No external libraries required
* (turtle, random, and time are built-in)

=> How to Run
python main.py

=> Concepts Used
* Object-Oriented Programming
* Inheritance
* Game loops
* Collision detection
* Randomization
* Event listeners

==> Author
MORTAZA PANAHI github acount (mortazap53)
