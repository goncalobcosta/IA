from board import *
from compound import *

class Level:
    def __init__(self, level):
        self.level = level
        
    def getLevelBoard(self):
        if (self.level == 0):
           
            h1 = Atom(H, (3, 2))
            h2 = Atom(H, (5, 2))
            h3 = Atom(H, (2, 6))
            h4 = Atom(H, (6, 6))
            c = Atom(C, (4, 5), True)
            
            hero = Compound([c], True)
            compounds = [Compound([h1]), Compound([h2]), Compound([h3]), Compound([h4])]

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

            return Board(9, 8, walls, blank, hero, compounds, {}, wallColor)
        
        elif (self.level == 1):
            
            o1 = Atom(O, (1, 1))
            o2 = Atom(O, (4, 4))
            c = Atom(C, (1, 4), True)
            
            hero = Compound([c], True)
            compounds = [Compound([o1]), Compound([o2])]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                (0, 1), (5, 1), 
                (0, 2), (5, 2),
                (0, 3), (5, 3),
                (0, 4), (5, 4),
                (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
            }

            circles = {
                (2, 2) : Circle(ADD)
            }

            wallColor = (94, 197, 228)
            
            return Board(6, 6, walls, {}, hero, compounds, circles, wallColor)
       
        elif (self.level == 2):
            h1 = Atom(H, (1, 5))
            h2 = Atom(H, (2, 6))
            h3 = Atom(H, (2, 3))
            h4 = Atom(H, (4, 5))
            c1 = Atom(C, (2, 5), True)
            c2 = Atom(C, (4, 3))
            o1 = Atom(O, (4, 1))
            o2 = Atom(O, (6, 3))
            
            c1.connections = [h1, h2]
            h1.connections = [c1]
            h2.connections = [c1]
            
            c1.updateImage()
            h1.updateImage()
            h2.updateImage()
            hero = Compound([c1, h1, h2], True)
            compounds = [Compound([h3]), Compound([h4]), Compound([o1]), Compound([o2]), Compound([c2])]

            walls = {
                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (1, 1), (7, 1), 
                (1, 2), (7, 2),
                (0, 3), (1, 3), (7, 3),
                (0, 4), (7, 4),
                (0, 5), (7, 5),
                (0, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7)
            }

            circles = {
                (3, 3) : Circle(ADD)
            }
            
            blank = {
                (0, 0), (0, 1), (0, 2), (5, 7), (6, 7), (7, 7)
            }

            wallColor = (94, 197, 228)
            
            return Board(8, 8, walls, blank, hero, compounds, circles, wallColor)
       