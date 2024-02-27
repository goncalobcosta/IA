from board import Board 
from piece import *

easy = Board(9, 8)

easy.grid = [ ["X", Wall(1, 0), Wall(2, 0), Wall(3, 0), Wall(4, 0), Wall(5, 0), Wall(6, 0), Wall(7, 0), "X"],
              [Wall(0, 1), Wall(1, 1), None, None, None, None, None, Wall(7, 1), Wall(8, 1)],
              [Wall(0, 2), None, None, Wall(3, 2), None, Wall(5, 2), None, None, Wall(8, 2)],
              [Wall(0, 3), None, None, Wall(3, 3), None, Wall(5, 3), None, None, Wall(8, 3)],
              [Wall(0, 4), None, None, None, None, None, None, None, Wall(8, 4)],
              [Wall(0, 5), None, None, None, None, None, None, None, Wall(8, 5)],
              [Wall(0, 6), Wall(1, 6), None, None, None, None, None, Wall(7, 6), Wall(8, 6)],
              ["X", Wall(1, 7), Wall(2, 7), Wall(3, 7), Wall(4, 7), Wall(5, 7), Wall(6, 7), Wall(7, 7), "X"],
            ]

