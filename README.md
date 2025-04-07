# 2D Game: Catch the Enemy

This is a simple 2D game built with Pygame, where the player controls a blue rectangle that must catch red enemies to score points. The game has a timer, and the player earns points by colliding with the enemies.

## Features

- **Player Movement**: Use the arrow keys to move the player (blue rectangle) in any direction.
- **Enemy Collision**: The game spawns random enemies (red rectangles). When the player touches an enemy, the score increases, and the enemy respawns in a random location.
- **Timer**: The game has a countdown timer. The player has a limited time to score as many points as possible.
- **Game Over Screen**: Once the timer reaches zero, a game over screen appears showing the player's score and options to restart the game or exit.
- **Restart Option**: Press the "R" key to restart the game after it's over.

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install Pygame via pip if you don't have it installed:

   ```bash
   pip install pygame
