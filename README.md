# Snake Game (Two-Player)

This project is a **Two-Player Snake Game** built using **Python** and **Turtle Graphics**. Players control separate snakes and compete to eat apples while avoiding collisions.

## Features
- **Two-player gameplay** with separate controls.
- **Apples spawn randomly**, increasing snake length and score.
- **Screen wrap-around**, allowing snakes to pass through edges.
- **Collision detection** for tail and head collisions.
- **Score tracking** displayed at the top of the screen.

## Controls
**Player 1 (White Snake)**:
- `W` - Move Up
- `S` - Move Down
- `A` - Move Left
- `D` - Move Right

**Player 2 (Yellow Snake)**:
- `Arrow Up` - Move Up
- `Arrow Down` - Move Down
- `Arrow Left` - Move Left
- `Arrow Right` - Move Right

## How the Game Works
1. Both players start with a small snake.
2. Apples randomly appear on the screen.
3. Eating an apple increases the snake's length and score.
4. Snakes wrap around the screen edges.
5. Collision detection:
   - If a snake hits its own tail, it resets and loses its score.
   - If a snake collides with the opponent's tail, it resets and loses its score.
   - If two snake heads collide, the larger snake absorbs the smaller one.

## Installation & Running the Game
1. **Ensure Python is installed** (Python 3 recommended).
2. Run the script using:
   ```sh
   python snake_game.py
   ```
3. Control your snake and compete with the opponent!

## Code Structure
- `create_snake(color, start_x)`: Creates a new snake with a given color.
- `move(snake)`: Moves the snake in its current direction.
- `grow_snake(snake, parts, color)`: Adds segments when an apple is eaten.
- `check_tail_collision(snake, parts)`: Checks if a snake collides with its own tail.
- `check_head_collision(snake1, snake2)`: Checks if the snakes collide head-to-head.
- `update_score()`: Updates the scoreboard.
- `reset_snake(snake, parts, start_x)`: Resets a snake after a collision.

## Future Improvements
- Add a **single-player mode** with AI opponent.
- Implement **different difficulty levels**.
- Add **sound effects and animations**.

## License
This project is **open-source** and free to modify for learning or personal use.

---
### Note:
- The game is designed for **fun and competitive gameplay** between two players.
- Snakes **cannot move in the opposite direction instantly** (e.g., moving left from right is restricted).

