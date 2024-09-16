# Snake Game - Python (Tkinter)

A simple Python Snake game built with Tkinter. Control the snake to collect food while avoiding collisions with walls or its own body. The game ends when the snake crashes, and your score increases with each piece of food collected.

## Features
- **Movement:** Control the snake using the arrow keys (Up, Down, Left, Right).
- **Food:** The snake grows as it eats food (red square).
- **Game Over:** Occurs when the snake hits the wall or itself.
- **Score:** Displayed at the top left.

## How to Play
- Use arrow keys to move.
- Collect food to grow.
- Avoid hitting the walls or your body.
- The score increases by 1 per food.

## Installation
Install Tkinter if needed:
```bash
pip install tk
```

Clone the repository:
```bash
git clone https://github.com/your_username/snake_game.git
```
## Run the game:
```
python snake_game.py
```
## Code Overview
- **Setup:** The game window is built using Tkinter.
- **Snake and Food:** Represented as tiles on a grid. The snake starts with one tile and grows with each food.
- **Game Loop:** draw() updates the snake, handles collisions, and renders the game elements.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/cb4cacc0-8642-4447-a960-c419c9994862" alt="image" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/2fd7752a-32a5-4cd5-9dae-587e4c85ee50" alt="image" width="400"/></td>
  </tr>
</table>


