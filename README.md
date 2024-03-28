# Sokobond with Pygame and AI

## Description:

Sokobond is a puzzle game where players push atoms around a grid, trying to create molecules by bonding atoms together. This implementation of Sokobond utilizes the Pygame library for graphics and user interaction, enhanced with an AI component to provide challenging gameplay.

## Features:

1. **Pygame Graphics:** Enjoy a visually appealing interface with smooth animations and intuitive controls.
2. **Puzzle Solving:** Exercise your brain with a variety of challenging puzzles that require strategic thinking to solve.
3. **AI Assistance:** For players seeking an extra challenge or hint, an AI component provides assistance in solving puzzles.
4. **Multiple Levels:** Explore a range of levels, each with increasing complexity, ensuring hours of engaging gameplay.
5. **Custom Levels:** Create and share custom levels, expanding the game's replayability and community engagement.
6. **Scoring System:** Track your progress and compete with friends by earning scores based on your puzzle-solving efficiency.

## Installation:

1. Ensure you have Python installed on your system.
2. Install the Pygame library using pip: `pip install pygame`.
3. Download the Sokobond game files from the repository.
4. Run the game script using Python: `python sokobond.py`.

## Controls:

- Use the arrow keys or WASD to move atoms.
- Press the 'R' key to restart a level.
- Access the AI assistance with the 'H' key.

## AI Assistance:

- The AI component provides hints and solutions to help you progress through challenging puzzles.
- Press the 'H' key to activate AI assistance, and it will suggest the next move or provide a complete solution if needed.

## Customization:

- Customize your gaming experience by creating and sharing custom levels.
- Explore new challenges by experimenting with different atom configurations and puzzle designs.

## Contributing:

- Contributions to the project are welcome! Fork the repository, make your changes, and submit a pull request.
- Bug reports and feature requests can be submitted via the issue tracker on the repository.

## Credits:

- Developed by [Your Name or Team Name].
- Powered by Pygame and Python.

## License:

- This game is released under the [License Name], allowing for free distribution and modification.

## Acknowledgments:

- Special thanks to the creators of Sokobond for the inspiration.
- Thanks to the Pygame community for the robust library that powers the game's graphics and interactions.

| Level | DFS | BFS | Best-First | Greedy | A\* |
| ----- | --- | --- | ---------- | ------ | --- |
| 1     | 14  | 27  | 0          | 15     | 23  |
| 2     | 24  | 23  | 0          | 20     | 21  |
| 3     | 102 | 77  | 0          | 100    | 62  |
| 4     | 151 | 459 | 0          | 105    | 391 |
| 5     | 38  | 62  | 14         | 32     | 59  |
| 6     | 24  | 166 | 0          | 39     | 107 |
| 7     | 30  | 219 | 0          | 222    | 148 |
| 8     | 54  | 263 | 0          | 152    | 249 |
| 9     | 24  | 72  | 17         | 60     | 66  |
| 10    | 187 | 340 | 0          | 533    | 305 |
