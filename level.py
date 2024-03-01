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

            return Board(9, 8, walls, blank, atoms, compound, {}, wallColor)
        
        elif (self.level == 1):

            atoms = {
                (5, 1) : Atom(H), 
                (5, 4) : Atom(H), 
                (2, 1) : Atom(N), 
            }

            compound = {
                (2, 4) : Atom(N, True)
            }

            walls = {
                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (1, 1), (6, 1), (7, 1), 
                (0, 2), (7, 2),
                (0, 3), (7, 3),
                (0, 4), (1, 4), (6, 4), (7, 4), 
                (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)
            }
            
            blank = {
                (0, 0), (7, 0), (0, 5), (7, 5)
            }

            circles = {
                (1, 2) : Circle(ROTATE),
                (4, 2) : Circle(ADD)
            }

            wallColor = (94, 197, 228)
            return Board(8, 6, walls, blank, atoms, compound, circles, wallColor)