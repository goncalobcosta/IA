from board import *

class Level:
    def __init__(self, level):
        self.level = level
        
    def getLevelBoard(self):
        if (self.level == 0):
            grid = [["X", "W", "W", "W", "W", "W", "W", "W", "X"],
                    ["W", "W", None, None, None, None, None, "W", "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", None, None, "W", None, "W", None, None, "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", "W", None, None, None, None, None, "W", "W"],
                    ["X", "W", "W", "W", "W", "W", "W", "W", "X"]
                    ]

            atoms = [Atom("hydrogen", (3, 2)), Atom("hydrogen", (5, 2)), Atom("hydrogen", (2, 6)), Atom("hydrogen", (6, 6))]
            compound = [Atom("carbon", (4, 5), True)] 
            wallColor = (239, 175, 26)
            return Board(9, 8, grid, atoms, compound, wallColor)
        
        elif (self.level == 1):
            grid = [["X", "W", "W", "W", "W", "W", "W", "X"],
                    ["W", "W", None, None, None, None, "W", "W"],
                    ["W", None, None, None, None, None, None, "W"],
                    ["W", None, None, None, None, None, None, "W"],
                    ["W", "W", None, None, None, None, "W", "W"],
                    ["X", "W", "W", "W", "W", "W", "W", "X"]
                    ]

            atoms = [Atom("hydrogen", (5, 1)), Atom("hydrogen", (5, 4)), Atom("nitrogen", (2, 1))]
            compound = [Atom("nitrogen", (2, 4), True)] 
            wallColor = (94, 197, 228)
            return Board(8, 6, grid, atoms, compound, wallColor)
        
        elif (self.level == 2):
            grid = [["X", "W", "W", "W", "W", "W", "W", "W", "X"],
                    ["W", "W", None, None, None, None, None, "W", "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", None, None, None, None, None, None, None, "W"],
                    ["W", "W", None, None, None, None, None, "W", "W"],
                    ["X", "W", "W", "W", "W", "W", "W", "W", "X"]
                    ]

            atoms = [Atom("hydrogen", (3, 2)), Atom("hydrogen", (5, 2)), Atom("hydrogen", (2, 6)), Atom("hydrogen", (6, 6))]
            compound = [Atom("carbon", (4, 5), True)] 
            wallColor = (40, 204, 153)
            return Board(9, 8, grid, atoms, compound, wallColor)
            
            