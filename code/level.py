from code.board import *
from code.compound import *

class Level:
    def __init__(self, level):
        self.level = level
        self.board = self.createBoard()
         
    def createBoard(self):
        if (self.level == 0):

            o = Atom(O, (4, 4))
            h1 = Atom(H, (2, 5), True)
            h2 = Atom(H, (6, 3))
            
            hero = Compound([h1], True)
            compounds = [
                Compound([h2]),
                Compound([o]),
            ]
            
            walls = {
                (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                (3, 1), (8, 1),
                (0, 2), (1, 2), (2, 2), (3, 2), (8, 2),
                (0, 3), (5, 3), (8, 3),    
                (0, 4), (5, 4), (8, 4),
                (0, 5), (8, 5),
                (0, 6), (5, 6), (6, 6), (7, 6), (8, 6),
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7)
            }

            blank = {
                (0, 0), 
                (1, 0),
                (2, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (6, 7),
                (7, 7),
                (8, 7),
            }
            wallColor = (44, 202, 151)

            return Board(9, 8, walls, blank, hero, compounds, {}, {}, {}, wallColor, "LET'S GO")
       
        elif (self.level == 2):
            
            h1 = Atom(H, (2, 1))
            h2 = Atom(H, (2, 3))
            h3 = Atom(H, (4, 3))
            n = Atom(N, (4, 1), True)
          
            
            hero = Compound([n], True)
            compounds = [
                Compound([h1]), 
                Compound([h2]), 
                Compound([h3]), 
            ]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (6, 1),
                (0, 2), (6, 2),
                (0, 3), (6, 3),
                (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
            }
            
            wallColor = (92, 93, 95)

            return Board(7, 5, walls, {}, hero, compounds, {}, {}, {}, wallColor, "PUSH")

        elif (self.level == 3):
            
            h1 = Atom(H, (2, 3), True)
            h2 = Atom(H, (4, 3))
            o1 = Atom(O, (3, 1))
            o2 = Atom(O, (3, 5))
          
            
            hero = Compound([h1], True)
            compounds = [
                Compound([h2]), 
                Compound([o1]), 
                Compound([o2]), 
            ]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (6, 1),
                (0, 2), (3, 2), (6, 2),
                (0, 3), (3, 3), (6, 3),
                (0, 4), (3, 4), (6, 4),
                (0, 5), (6, 5),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
            }
            
            wallColor = (92, 93, 95)

            return Board(7, 7, walls, {}, hero, compounds, {}, {}, {}, wallColor, "PUSH")

         