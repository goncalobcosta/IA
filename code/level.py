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

            return Board(9, 8, walls, blank, hero, compounds, set(), set(), set(), wallColor, "LET'S GO")
       
        elif (self.level == 1):
            
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

            return Board(7, 5, walls, set(), hero, compounds, set(), set(), set(), wallColor, "STRUCTURE")

        elif (self.level == 2):
            
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

            return Board(7, 7, walls, set(), hero, compounds, set(), set(), set(), wallColor, "LOOP")
    
        elif (self.level == 3):
            
            h1 = Atom(H, (2, 2), True)
            h2 = Atom(H, (3, 1))
            h3 = Atom(H, (4, 2))
            n = Atom(N, (3, 3))
          
            
            hero = Compound([h1], True)
            compounds = [
                Compound([n]), 
                Compound([h2]), 
                Compound([h3]), 
            ]

            walls = {
                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (1, 1), (6, 1),
                (0, 2), (3, 2), (6, 2),
                (0, 3), (6, 3),
                (0, 4), (6, 4),
                (0, 5), (6, 5),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
            }
            
            wallColor = (92, 93, 95)

            blank = { (0, 0) }
            return Board(7, 7, walls, blank, hero, compounds, set(), set(), set(), wallColor, "BLOCK")

        elif (self.level == 4):
            
            h1 = Atom(H, (3, 3))
            h2 = Atom(H, (5, 3))
            h3 = Atom(H, (3, 5))
            h4 = Atom(H, (5, 5))
            c = Atom(C, (4, 1), True)
        
            hero = Compound([c], True)
            compounds = [
                Compound([h1]), 
                Compound([h2]), 
                Compound([h3]), 
                Compound([h4]), 
            ]

            walls = {
                (3, 0), (4, 0), (5, 0),
                (2, 1), (3, 1), (5, 1), (6, 1),
                (1, 2), (2, 2), (6, 2), (7, 2),
                (0, 3), (1, 3), (7, 3), (8, 3),
                (0, 4), (8, 4),
                (0, 5), (1, 5), (7, 5), (8, 5),
                (1, 6), (2, 6), (6, 6), (7, 6),
                (2, 7), (3, 7), (5, 7), (6, 7),
                (3, 8), (4, 8), (5, 8),
            }
            
            wallColor = (92, 93, 95)

            blank = {
                (0, 0), (1, 0), (2, 0), (6, 0), (7, 0), (8, 0),
                (0, 1), (1, 1), (7, 1), (8, 1),
                (0, 2), (8, 2),
                (0, 6), (8, 6),
                (0, 7), (1, 7), (7, 7), (8, 7),
                (0, 8), (1, 8), (2, 8), (6, 8), (7, 8), (8, 8)
            }

            return Board(9, 9, walls, blank, hero, compounds, set(), set(), set(), wallColor, "LOOP")

         
        elif (self.level == 5):
            
            h1 = Atom(H, (1, 4), True)
            h2 = Atom(H, (1, 1))
            h3 = Atom(H, (4, 1))
            h4 = Atom(H, (4, 4))
        
            hero = Compound([h1], True)
            compounds = [
                Compound([h2]), 
                Compound([h3]), 
                Compound([h4]), 
            ]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                (0, 1), (5, 1),
                (0, 2), (5, 2),
                (0, 3), (5, 3),
                (0, 4), (5, 4),
                (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
            }
            
            wallColor = (92, 93, 95)

            red = {(2, 2)}
            return Board(6, 6, walls, set(), hero, compounds, red, set(), set(), wallColor, "MULTIPLE")

        elif (self.level == 6):
            
            o1 = Atom(O, (1, 1))
            o2 = Atom(O, (4, 4))
            c = Atom(C, (1, 4), True)
        
            hero = Compound([c], True)
            compounds = [
                Compound([o1]), 
                Compound([o2]), 
            ]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                (0, 1), (5, 1),
                (0, 2), (5, 2),
                (0, 3), (5, 3),
                (0, 4), (5, 4),
                (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
            }
            
            wallColor = (92, 93, 95)

            green = {(2, 2)}
            return Board(6, 6, walls, set(), hero, compounds, set(), green, set(), wallColor, "MULTIPLE")
        
        elif (self.level == 7):
            
            h1 = Atom(H, (1, 3), True)
            h2 = Atom(H, (1, 1))
            o = Atom(O, (4, 1))
        
            hero = Compound([h1], True)
            compounds = [
                Compound([h2]), 
                Compound([o]) 
            ]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                (0, 1), (5, 1),
                (0, 2), (5, 2),
                (0, 3), (3, 3), (4, 3), (5, 3),
                (0, 4), (1, 4), (2, 4), (3, 4)
            }
            
            wallColor = (92, 93, 95)

            blank = {(4, 4), (5, 4)}

            return Board(6, 5, walls, blank, hero, compounds, set(), set(), set(), wallColor, "CELL")
        
        elif (self.level == 8):
            
            h1 = Atom(H, (2, 1))
            h2 = Atom(H, (6, 1))
            h3 = Atom(H, (2, 3))
            h4 = Atom(H, (6, 3))
            c = Atom(C, (4, 2), True)
        
            hero = Compound([c], True)
            compounds = [
                Compound([h1]), 
                Compound([h2]), 
                Compound([h3]), 
                Compound([h4]), 
            ]

            walls = {
                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (1, 1), (7, 1), (8, 1),
                (0, 2), (8, 2),
                (0, 3), (1, 3), (7, 3), (8, 3),
                (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
            }
            
            wallColor = (92, 93, 95)

            blank = {(0, 0), (8, 0), (0, 4), (8, 4)}

            return Board(9, 5, walls, blank, hero, compounds, set(), set(), set(), wallColor, "KNOT")
        
         
        elif (self.level == 9):
            
            h1 = Atom(H, (3, 2))
            h2 = Atom(H, (5, 2))
            o = Atom(O, (1, 2), True)
        
            hero = Compound([o], True)
            compounds = [
                Compound([h1]), 
                Compound([h2])
            ]

            walls = {
                (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (1, 1), (2, 1), (6, 1), (7, 1),
                (0, 2), (7, 2),
                (0, 3), (1, 3), (2, 3), (6, 3), (7, 3),
                (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
            }
            
            wallColor = (92, 93, 95)

            blank = {
                (0, 0), (1, 0), (7, 0),
                (0, 4), (1, 4), (7, 4)
            }

            return Board(8, 5, walls, blank, hero, compounds, set(), set(), set(), wallColor, "PUSH")