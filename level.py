from board import *

class Level:
    def __init__(self, level):
        self.level = level
        
    def getLevelBoard(self):
        if (self.level == 0):
           
            atoms = {
                (3, 2) : Atom(H), 
                (5, 2) : Atom(H), 
                (2, 6) : Atom(H), 
                (6, 6) : Atom(H)
            }

            compound = {
                (4, 5) : Atom(C, True)
            }

            walls = {
                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (1, 1), (7, 1), (8, 1), 
                (0, 2), (8, 2),
                (0, 3), (3, 3), (5, 3), (8, 3),
                (0, 4), (8, 4),
                (0, 5), (8, 5),
                (0, 6), (1, 6), (7, 6), (8, 6), 
                (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
            }
            
            blank = {
                (0, 0), (8, 0), (0, 7), (8, 7)
            }

            wallColor = (239, 175, 26)
  
            circles = {
                (5, 5) : Circle(BREAK),
                (5, 6) : Circle(ADD),
                (6, 7) : Circle(ROTATE),
            }

            return Board(9, 8, walls, blank, atoms, compound, {}, wallColor)
        
        