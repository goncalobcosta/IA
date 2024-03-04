from code.board import *
from code.compound import *

class Level:
    def __init__(self, level):
        self.level = level
        self.board = self.createBoard()
        
    def createBoard(self):
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
                (2, 2)
            }

            wallColor = (94, 197, 228)
            
            return Board(6, 6, walls, {}, hero, compounds, circles, {}, {}, wallColor)
       
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

            green = {
                (3, 3)
            }
            
            blank = {
                (0, 0), (0, 1), (0, 2), (5, 7), (6, 7), (7, 7)
            }

            wallColor = (94, 197, 228)
            
            return Board(8, 8, walls, blank, hero, compounds, {}, green, {}, wallColor)
        elif (self.level == 3):
            h1 = Atom(H, (1, 1))
            h2 = Atom(H, (1, 6))
            h3 = Atom(H, (6, 1))
            h4 = Atom(H, (6, 6))
            c = Atom(C, (4, 3))
            o = Atom(O, (3, 4), True)
            
            hero = Compound([o], True)
            compounds = [Compound([h1]), Compound([h2]), Compound([h3]), Compound([h4]), Compound([c])]

            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (7, 1), 
                (0, 2), (7, 2),
                (0, 3), (7, 3),
                (0, 4), (7, 4),
                (0, 5), (7, 5),
                (0, 6), (7, 6),
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)
            }

            red = {
                (3, 3)
            }
            
            wallColor = (94, 197, 228)
            
            return Board(8, 8, walls, {}, hero, compounds, red, {}, {}, wallColor)
        
        elif (self.level == 4):

            o1 = Atom(O, (2, 1), True)
            o2 = Atom(O, (2, 2))
            o3 = Atom(O, (1, 2))
            o4 = Atom(O, (4, 4))

            o1.connections = [o2]
            o2.connections = [o1, o3]
            o3.connections = [o2]

            o1.updateImage()
            o2.updateImage()
            o3.updateImage()

            hero = Compound([o1, o2, o3], True)
            compounds = [Compound([o4])]
            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                (0, 1), (5, 1), 
                (0, 2), (5, 2),
                (0, 3), (5, 3),
                (0, 4), (5, 4),
                (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
              }

            red = {
                (1, 1),
                (2, 1),
                (3, 1),
                (1, 2),
                (2, 2),
                (3, 2),
                (1, 3),
                (2, 3),
                (3, 3),
            }

            wallColor = (94, 197, 228)

            return Board(6, 6, walls, {}, hero, compounds, red, {}, {}, wallColor)
       
        elif (self.level == 5):

            he1 = Atom(He, (4, 1))
            he2 = Atom(He, (3, 2))
            he3 = Atom(He, (2, 3))
            he4 = Atom(He, (1, 4))
            he5 = Atom(He, (3, 4))
            he6 = Atom(He, (4, 3))
            he7 = Atom(He, (5, 4))
            he8 = Atom(He, (6, 3))
            he9 = Atom(He, (4, 5))
            he10 = Atom(He, (3, 6))
            o1 = Atom(O, (2, 2))
            o2 = Atom(O, (5, 2))
            h1 = Atom(H, (2, 5), True)
            h2 = Atom(H, (5, 5))       
    


            hero = Compound([h1], True)
            compounds = [
                Compound([he1]),
                Compound([he2]),
                Compound([he3]),
                Compound([he4]),
                Compound([he5]),
                Compound([he6]),
                Compound([he7]),
                Compound([he8]),
                Compound([he9]),
                Compound([he10]),
                Compound([o1]),
                Compound([o2]),
                Compound([h2]),
                ]
            
            walls = {
                (2, 0), (3, 0), (4, 0), (5, 0),
                (1, 1), (2, 1), (5, 1), (6, 1), 
                (0, 2), (1, 2), (6, 2), (7, 2), 
                (0, 3), (7, 3),
                (0, 4), (7, 4),
                (0, 5), (1, 5), (6, 5), (7, 5), 
                (1, 6), (2, 6), (5, 6), (6, 6), 
                (2, 7), (3, 7), (4, 7), (5, 7),
              }

        
            wallColor = (94, 197, 228)

            blank = {
                (0, 0), (1, 0), (6, 0), (7, 0), 
                (0, 1), (7, 1), 
                (0, 6), (7, 6),
                (0, 7), (1, 7), (6, 7), (7, 7), 
            }

            return Board(8, 8, walls, blank, hero, compounds, {}, {}, {}, wallColor)
        elif (self.level == 6):

            h1 = Atom(H, (2, 4))
            h2 = Atom(H, (2, 6))
            o1 = Atom(O, (4, 1), True)
            o2 = Atom(O, (8, 1))

            hero = Compound([o1], True)
            compounds = [
                Compound([h1]),
                Compound([h2]),
                Compound([o2]),
                ]
            
            walls = {
                (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
                (3, 1), (6, 1), (9, 1), 
                (3, 2), (9, 2),
                (0, 3), (1, 3), (2, 3), (3, 3), (9, 3),
                (0, 4), (3, 4), (9, 4),
                (0, 5), (9, 5),
                (0, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6),
                (0, 7), (1, 7), (2, 7), (3, 7)
              }

            red = {
                (5, 1), (6, 1)
            }

            green = {
                (7, 1), (7, 2), (7, 3), (6, 2), (6, 4), (5, 3), (5, 4), (4, 2), (4, 3), (4, 4)
            }

            wallColor = (94, 197, 228)

            blank = {
                (0, 0), (1, 0), (2, 0),
                (0, 1), (1, 1), (2, 1),
                (0, 2), (1, 2), (2, 2),
                (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)
            }

            return Board(10, 8, walls, blank, hero, compounds, red, green, {}, wallColor)
        elif (self.level == 7):

            h1 = Atom(H, (2, 2))
            h2 = Atom(H, (6, 2))
            h3 = Atom(H, (1, 4))
            h4 = Atom(H, (7, 4))
            h5 = Atom(H, (2, 6)) 
            h6 = Atom(H, (6, 6))
            h7 = Atom(H, (3, 7))
            h8 = Atom(H, (5, 7))
            o = Atom(O, (4, 1), True)
            c1 = Atom(C, (2, 4))
            c2 = Atom(C, (4, 4))
            c3 = Atom(C, (6, 4))

            c1.connections = [h3]
            h3.connections = [c1]

            c3.connections = [h4]
            h4.connections = [c3]

            h3.updateImage()
            h4.updateImage()
            c1.updateImage()
            c3.updateImage()

            hero = Compound([o], True)
            compounds = [
                Compound([h1]),
                Compound([h2]),
                Compound([h3, c1]),
                Compound([h4, c3]),
                Compound([c2]),
                Compound([h5]),
                Compound([h6]),
                Compound([h7]),
                Compound([h8]),
            ]
            
            walls = {
                (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (1, 1), (2, 1), (6, 1), (7, 1), (8, 1),
                (0, 2), (8, 2),
                (0, 3), (8, 3),
                (0, 4), (8, 4),
                (0, 5), (8, 5),
                (0, 6), (8, 6),
                (0, 7), (8, 7),
                (0, 8), (8, 8),
                (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9),
            }

            wallColor = (94, 197, 228)

            blank = {
                (0, 0), (1, 0), (7, 0), (8, 0)
            }

            return Board(9, 10, walls, blank, hero, compounds, {}, {}, {}, wallColor)
       