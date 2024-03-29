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
            
            wallColor = (239, 175, 26)

            blank = {
                (0, 0), (1, 0), (7, 0),
                (0, 4), (1, 4), (7, 4)
            }

            return Board(8, 5, walls, blank, hero, compounds, set(), set(), set(), wallColor, "PUSH") 
        elif (self.level == 1):
            
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
            
            wallColor = (95, 175, 95)

            green = {(2, 2)}
            return Board(6, 6, walls, set(), hero, compounds, set(), green, set(), wallColor, "SIMILAR")      
        elif (self.level == 2):
            
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
            
            wallColor = (122, 207, 119)

            blank = {(4, 4), (5, 4)}

            return Board(6, 5, walls, blank, hero, compounds, set(), set(), set(), wallColor, "CELL")       
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

            return Board(7, 7, walls, set(), hero, compounds, set(), set(), set(), wallColor, "LOOP")
        elif (self.level == 4):
            
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
            
            wallColor = (72, 52, 132)

            red = {(2, 2)}
            return Board(6, 6, walls, set(), hero, compounds, red, set(), set(), wallColor, "MULTIPLE")
        elif (self.level == 5):

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
            wallColor = (142, 142, 142)

            return Board(9, 8, walls, blank, hero, compounds, set(), set(), set(), wallColor, "LET'S GO")       
        elif (self.level == 6):
            
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
            
            wallColor = (254, 114, 113)

            blank = {(0, 0), (8, 0), (0, 4), (8, 4)}

            return Board(9, 5, walls, blank, hero, compounds, set(), set(), set(), wallColor, "KNOT")
        elif (self.level == 7):
            
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
            
            wallColor = (255, 210, 82)

            return Board(7, 5, walls, set(), hero, compounds, set(), set(), set(), wallColor, "STRUCT")
        elif (self.level == 8):
            
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
            
            wallColor = (94, 197, 228)

            blank = {
                (0, 0), (1, 0), (2, 0), (6, 0), (7, 0), (8, 0),
                (0, 1), (1, 1), (7, 1), (8, 1),
                (0, 2), (8, 2),
                (0, 6), (8, 6),
                (0, 7), (1, 7), (7, 7), (8, 7),
                (0, 8), (1, 8), (2, 8), (6, 8), (7, 8), (8, 8)
            }

            return Board(9, 9, walls, blank, hero, compounds, set(), set(), set(), wallColor, "NEWBIE")
        elif (self.level == 9):
            
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
            
            wallColor = (44, 202, 151)

            blank = { (0, 0) }
            return Board(7, 7, walls, blank, hero, compounds, set(), set(), set(), wallColor, "BLOCK")  
        elif (self.level == 10):
           
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
            
            return Board(9, 8, walls, blank, hero, compounds, set(), set(), set(), wallColor, "CREATURE")     
        elif (self.level == 11):
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

            wallColor = (122, 207, 119)
            
            return Board(8, 8, walls, blank, hero, compounds, set(), green, set(), wallColor, "LETTUCE")
        elif (self.level == 12):
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
            
            wallColor = (255, 210, 82)
            
            return Board(8, 8, walls, set(), hero, compounds, red, set(), set(), wallColor, "WINGMAN")
        elif (self.level == 13):

            o1 = Atom(O, (1, 5))
            o2 = Atom(O, (1, 1))
            o3 = Atom(O, (5, 1))
            o4 = Atom(O, (5, 5), True)

            hero = Compound([o4], True)
            compounds = [Compound([o1]), Compound([o2]), Compound([o3])]
            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                (0, 1), (6, 1), 
                (0, 2), (6, 2),
                (0, 3), (6, 3),
                (0, 4), (6, 4),
                (0, 5), (6, 5),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)
              }

            blue = {
                (1, 1),
                (2, 1),
                (3, 1),
                (1, 2),
                (2, 2),
                (3, 2),
                (1, 3),
                (2, 3),
                (3, 3),
                (1, 4),
                (2, 4),
                (3, 4),
                (4, 4),
                (4, 1),
                (4, 2),
                (4, 3)
            }

            wallColor = (94, 197, 228)

            return Board(7, 7, walls, set(), hero, compounds, set(), set(), blue, wallColor, "SNAKE")
        elif (self.level == 14):

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

        
            wallColor = (142, 142, 142)

            blank = {
                (0, 0), (1, 0), (6, 0), (7, 0), 
                (0, 1), (7, 1), 
                (0, 6), (7, 6),
                (0, 7), (1, 7), (6, 7), (7, 7), 
            }

            return Board(8, 8, walls, blank, hero, compounds, set(), set(), set(), wallColor, "CLOUD")
        elif (self.level == 15):

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

            wallColor = (95, 175, 95)

            blank = {
                (0, 0), (1, 0), (2, 0),
                (0, 1), (1, 1), (2, 1),
                (0, 2), (1, 2), (2, 2),
                (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)
            }

            return Board(10, 8, walls, blank, hero, compounds, red, green, set(), wallColor, "MINE FIELD")
        elif (self.level == 16):

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

            wallColor = (72, 52, 132)

            blank = {
                (0, 0), (1, 0), (7, 0), (8, 0)
            }

            return Board(9, 10, walls, blank, hero, compounds, set(), set(), set(), wallColor, "SLAM")
        elif (self.level == 17):

            h = Atom(H, (2, 7), True)
            n = Atom(N, (3, 2))
            o1 = Atom(O, (3, 6))
            o2 = Atom(O, (7, 6))

            hero = Compound([h], True)
            compounds = [
                Compound([n]),
                Compound([o1]),
                Compound([o2]),
            ]
            
            walls = {
                (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
                (1, 1), (9, 1),
                (1, 2), (9, 2),
                (1, 3), (9, 3),
                (0, 4), (1, 4), (2, 4), (4, 4), (5, 4), (9, 4),
                (0, 5), (5, 5), (9, 5),
                (0, 6), (9, 6),
                (0, 7), (5, 7), (9, 7),
                (0, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8),
                (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)
            }

            blank = {
                (0, 0), (0, 1), (0, 2), (0, 3),
                (6, 9), (7, 9), (8, 9), (9, 9)
            }

            green = {
                (7, 1)
            }

            wallColor = (254, 114, 113)

            return Board(10, 10, walls, blank, hero, compounds, set(), green, set(), wallColor, "APART")
        elif (self.level == 18):
            
            h1 = Atom(H, (5, 1))
            h2 = Atom(H, (7, 1))
            h3 = Atom(H, (5, 8))
            h4 = Atom(H, (7, 8))
            o1 = Atom(O, (2, 5), True)
            o2 = Atom(O, (2, 4))
            he1 = Atom(He, (5, 4))
            he2 = Atom(He, (5, 5))
            
            o1.connections = [o2]
            o2.connections = [o1]

            o1.updateImage()
            o2.updateImage()

            hero = Compound([o1, o2], True)
            compounds = [
                Compound([h1]), 
                Compound([h2]), 
                Compound([h3]), 
                Compound([h4]),
                Compound([he1]), 
                Compound([he2]),
            ]

            walls = {
                (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), 
                (4, 1), (8, 1), 
                (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (7, 2), (8, 2), 
                (0, 3), (4, 3), (8, 3),
                (0, 4), (8, 4),
                (0, 5), (8, 5),
                (0, 6), (4, 6), (8, 6),
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (7, 7), (8, 7), 
                (4, 8), (8, 8),
                (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), 
            }
            
            blank = {
                (0, 0), (1, 0), (2, 0), (3, 0),
                (0, 1), (1, 1), (2, 1), (3, 1),
                (0, 8), (1, 8), (2, 8), (3, 8),
                (0, 9), (1, 9), (2, 9), (3, 9),
            }

            red = {
                (3, 4)
            }

            wallColor = (92, 93, 95)

            return Board(9, 10, walls, blank, hero, compounds, red, set(), set(), wallColor, "SPACESHIP")
        elif (self.level == 19):

            h1 = Atom(H, (2, 3))
            h2 = Atom(H, (6, 3))
            h3 = Atom(H, (1, 4))
            h4 = Atom(H, (7, 4))
            h5 = Atom(H, (2, 5)) 
            h6 = Atom(H, (6, 5))
            he = Atom(He, (4, 4), True)
            n1 = Atom(N, (4, 2))
            n2 = Atom(N, (4, 6))
            
            hero = Compound([he], True)
            compounds = [
                Compound([h1]),
                Compound([h2]),
                Compound([h3]),
                Compound([h4]),
                Compound([h5]),
                Compound([h6]),
                Compound([n1]),
                Compound([n2]),
            ]
            
            walls = {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                (0, 1), (4, 1), (8, 1),
                (0, 2), (2, 2), (6, 2), (8, 2),
                (0, 3), (8, 3),
                (0, 4), (2, 4), (6, 4), (8, 4),
                (0, 5), (8, 5),
                (0, 6), (2, 6), (6, 6), (8, 6),
                (0, 7), (4, 7), (8, 7),
                (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
            }

            wallColor = (44, 202, 151)

            return Board(9, 9, walls, set(), hero, compounds, set(), set(), set(), wallColor, "BUTTERFLY")