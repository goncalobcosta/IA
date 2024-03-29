# Sokobond with heuristic Search Methods 

<div style="text-align: center;">
    <img src="resources/images/sokobond.avif" style="height:400px;" alt="sokobond">
</div>

- [Sokobond with heuristic Search Methods](#sokobond-with-heuristic-search-methods)
  - [Summary](#summary)
  - [Installation and usage](#installation-and-usage)
  - [Features](#features)
  - [Definition of the game](#definition-of-the-game)
  - [Formulation of the problem as a search problem](#formulation-of-the-problem-as-a-search-problem)
  - [Game Controls](#game-controls)
  - [Hint - AI Assistance](#hint---ai-assistance)
  - [Algorithms controls](#algorithms-controls)
  - [Contributing:](#contributing)
  - [Credits:](#credits)
  - [License:](#license)
  - [Acknowledgments:](#acknowledgments)


## Summary

The project focuses on developing heuristic search methods for solving one-player solitaire games, with **Sokobond** being the chosen game for implementation. Utilizing Python along with the Pygame library, the project aims to provide both a playable solitaire game for human players and an automated solver capable of tackling various levels of Sokobond puzzles.

In addition to creating an engaging gaming experience, the project emphasizes the implementation of heuristic search algorithms for solving Sokobond puzzles efficiently. Special attention is given to comparing different uninformed search methods to evaluate their effectiveness in solving the game's puzzles.


By combining game development with artificial intelligence techniques, the project provides a platform for exploring and understanding heuristic search methods in the context of puzzle-solving games. Through experimentation and analysis, the project aims to shed light on the strengths and limitations of various search algorithms in tackling challenging solitaire game scenarios.

## Installation and usage

1. Ensure you have Python installed on your system.
2. Install the Pygame library using pip: `pip install pygame`.
3. Download the Sokobond game files from the repository.
4. Run the game script using Python: `python sokobond.py`.

## Features



## Definition of the game

**Sokobond** is a puzzle game with a chemistry theme. It involves using logic and planning to move atoms around a 2D grid to form specific chemical compounds. Even though the game is centered around creating molecules, you don't need any prior knowledge of chemistry to play and enjoy it.

There are five elements introduced: 
- **He** : Helium (0 bonds)
- **H** : Hydrogen (1 bond)
- **O** : Oxygen (2 bonds)
- **N** : Nitrogen (3 bonds)
- **C** : Carbon (4 bonds)

There are also 3 powerups in the game:

- 🔵 -> turns the molecule into a snake (if possible)
    
- 🟢 -> Duplicate the connection (if possible)

- 🔴 -> Cut the connection.


## Formulation of the problem as a search problem

- **State representation** : Board with the molecules distributed in their respective positions.

- **Initial State** : Board with the molecules distributed in their respective initial positions.

- **Objective Test** : All atoms present on the board with no valence electrons (available bonds) remaining.

- **Operators** : Move the atom (Hero) to
     - **Up**. Precondition: the atom can move upwards. Cost: 1.
     - **Down**. Precondition: the atom can move downwards. Cost: 1.
     - **Left**. Precondition: the atom can move to the left. Cost: 1.
     - **Right**. Precondition: the atom can move to the right. Cost: 1.
      
- **Solution Cost** : Total number of moves required to reach the objective test.
  

## Game Controls

- **Movement** : Use the arrow keys to move the hero atom.
- **Reset Level** : Press the '**R**' key.
- **Hint** : Press the '**H**' key.
- **Level Menu** : Press the '**L**' key.
- **Main Menu**: Press the '**M**' key.
- **Quit Game** : Press the '**Q**' key.


## Hint - AI Assistance

- The AI component provides hints and solutions to help you progress through challenging puzzles, using the A* algorithm.
- Press the 'H' key to activate AI assistance, and it will suggest the next move.

## Algorithms controls

- **Depth-First Search** : Press the '**1**' key.
- **Breadth-First Search** : Press the '**2**' key.
- **Best-first Search** : Press the '**3**' key.
- **Greedy Algorithm**: Press the '**4**' key.
- **A* Algorithm** : Press the '**5**' key.
    
After selecting the algorithm, the AI assistant will automatically solve the level, displaying the chosen solution step by step.

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

| Level | DFS                | BFS                | Best-First          | Greedy             | A\*                |
| ----- | ------------------ | ------------------ | ------------------- | ------------------ | ------------------ |
| 1     | 0.8021419048309326 | 1.0106089115142822 | 0.4763469696044922  | 0.3754098415374756 | 0.7470529079437256 |
| 2     | 1.4383280277252197 | 1.1336913108825684 | 0.21555876731872559 | 0.7591400146484375 | 0.9220609664916992 |
| 3     | 7.939976930618286  | 4.083004951477051  | 0.45690393447875977 | 4.990835189819336  | 2.7785332202911377 |
| 4     | 13.650975942611694 | 22.883535861968994 | 0.9361181259155273  | 3.2408690452575684 | 17.079802751541138 |
| 5     | 2.018979787826538  | 2.9781649112701416 | 0.7404899597167969  | 0.8506731986999512 | 2.1123809814453125 |
| 6     | 1.3543281555175781 | 6.913877964019775  | 1.072571039199829   | 1.369917869567871  | 4.216050386428833  |
| 7     | 1.898435115814209  | 9.830797910690308  | 1.2657060623168945  | 7.939723968505859  | 6.384228229522705  |
| 8     | 4.700311183929443  | 18.000312089920044 | 1.117546796798706   | 9.00442123413086   | 16.560086965560913 |
| 9     | 1.5436511039733887 | 4.392554998397827  | 1.0736608505249023  | 3.6003708839416504 | 3.9867048263549805 |
| 10    | 14.377259016036987 | 19.581570148468018 | 0.9953858852386475  | 28.475540161132812 | 16.36307406425476  |
