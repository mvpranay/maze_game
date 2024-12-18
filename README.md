# Maze Game 🐇🎮

A 2D maze game developed using **pygame**, where you guide a rabbit through an underground maze to reach the golden carrot while managing energy and time.

---

## Introduction
The Maze Game is a Python project designed for an engaging gaming experience with three levels of difficulty: **Easy**, **Medium**, and **Hard**. Players must navigate the rabbit through mazes while eating carrots to replenish energy, avoiding starvation, and completing the level within a set time limit.

---

## Features
- **Dynamic maze generation**: Uses three algorithms:
  - Binary Tree (Easy)
  - Prim’s Algorithm (Medium)
  - Recursive Backtracking (Hard)
- **Energy management**: Consume carrots to replenish energy.
- **Progressive challenges**: Increasing difficulty with fewer resources.
- **Smooth animations**: Centered rabbit with tile-to-tile jumping.
- **Immersive sound**: Background music and action-specific sound effects.
- **Timer-based gameplay**: Visual countdown from green to red as time depletes.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mvpranay/maze_game.git
   cd maze-game
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python game.py
   ```

---

## How to Play
- Use **arrow keys** or **WASD keys** to navigate the rabbit through the maze.
- The objective is to reach the golden carrot while:
  - Collecting carrots to replenish energy.
  - Completing the maze before the timer runs out.
- Energy depletion slows down the rabbit and limits its movement.

---

## Game Levels
- **Easy**: 
  - Maze generated using the Binary Tree algorithm.
  - Time limit: **60 seconds**.
- **Medium**: 
  - Maze generated using Prim’s Algorithm.
  - Time limit: **100 seconds**.
- **Hard**: 
  - Maze generated using Recursive Backtracking.
  - Time limit: **150 seconds**.

---

## Graphics and Sound
- The rabbit remains centered in the screen with smooth tile-to-tile transitions.
- Sound effects:
  - Movement and carrot consumption.
  - Calming background music enhances gameplay.

---

## Project Structure
- **Python Files**:
  - `cell.py`: Defines the `Cell` class.
  - `wall.py`: Defines the `Wall` class.
  - `player.py`: Defines the `Player` class.
  - `constants.py`: Contains game constants.
  - `recursive_backtracking.py`: Maze generation using recursive backtracking.
  - `binary_tree.py`: Maze generation using Binary Tree algorithm.
  - `prims.py`: Maze generation using Prim’s algorithm.
  - `main_menu.py`: Displays the main menu.
  - `end_screen.py`: Displays the end screen.
  - `game_mechanics.py`: Core game logic.
  - `game.py`: Main game loop.
- **Resources**:
  - `audio/`: Contains game audio files.
  - `imgs/`: Contains game image files.
  - `path.txt`: Logs the maze solution path during gameplay.

---

## References
1. [Jamis Buck’s Blog](https://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap)
2. [Pygame Documentation](https://www.pygame.org/docs/)
3. ChatGPT and GitHub Copilot
