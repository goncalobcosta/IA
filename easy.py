import Board 

board = Board(9, 8)

board.grid = [[None, Wall, Wall, Wall, Wall, Wall, Wall, Wall, None],
              [Wall, Wall, None, None, None, None, None, Wall, Wall],
              [Wall, None, None, Hydrogen, None, Hydrogen, None, None, Wall],
              [Wall, None, None, Wall, None, Wall, None, None, Wall],
              [Wall, None, None, None, None, None, None, None, Wall],
              [Wall, None, None, None, None, None, None, None, Wall],
              [Wall, Wall, Hydrogen, None, None, None, Hydrogen, Wall, Wall],
              [None, Wall, Wall, Wall, Wall, Wall, Wall, Wall, None] 
            ]

