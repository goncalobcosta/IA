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

Solution Cost

| Level | DFS | BFS | Best-First | Greedy | A\* |
| ----- | --- | --- | ---------- | ------ | --- |
| 1     | 24  | 8   | 14         | 10     | 8   |
| 2     | 9   | 7   | 0          | 7      | 7   |
| 3     | 16  | 16  | 17         | 17     | 16  |
| 4     | 25  | 19  | 0          | 19     | 19  |
| 5     | 21  | 9   | 0          | 9      | 9   |
| 6     | 28  | 10  | 0          | 36     | 10  |
| 7     | 22  | 9   | 0          | 11     | 9   |
| 8     | 6   | 6   | 0          | 6      | 6   |
| 9     | 18  | 12  | 0          | 12     | 12  |
| 10    | 6   | 6   | 0          | 6      | 6   |

State Space explored
| Level | DFS | BFS | Best-First | Greedy | A\* |
| --- | --- | --- | --- | --- | --- |
| 1 | 38 | 118 | 15 | 48 | 99 |
| 2 | 102 | 142 | 7 | 179 | 106 |
| 3 | 24 | 140 | 18 | 116 | 128 |
| 4 | 187 | 652 | 16 | 989 | 566 |
| 5 | 151 | 766 | 12 | 148 | 619 |
| 6 | 30 | 374 | 20 | 347 | 249 |
| 7 | 24 | 287 | 19 | 63 | 181 |
| 8 | 24 | 44 | 4 | 34 | 38 |
| 9 | 54 | 507 | 15 | 272 | 470 |
| 10 | 14 | 46 | 9 | 22 | 37 |
