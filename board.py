import pygame
from compound import *
from circle import *

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (150, 150, 150)
GRAY = (192, 192, 192)
RED = (255, 138, 128)
YELLOW = (254, 216, 119)
BLUE = (166, 197, 254)
GREEN = (175, 219, 140)
BACKGROUND = (243, 243, 243)

class Board:
    def __init__(self, width, height, walls, blank, hero, compounds, circles, wallColor):
        self.width = width
        self.height = height
        self.walls = walls
        self.blank = blank
        self.hero = hero
        self.compounds = compounds
        self.circles = circles
        self.wallColor = wallColor
        
    def inBoard(self, pos):
        return (0 <= pos[0] < self.width and 0 <= pos[1] < self.height) and (pos not in self.blank) and (pos not in self.walls)
    
    
    def canMove(self, move, compound):
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            if not self.inBoard(nextPos):
                return False
            
            for other in self.compounds:
                if(other == compound): continue
                if other.isInPosition(nextPos) and ((len(compound.atoms) < len(other.atoms)) or not self.canMove(move, other)):
                    print("There is a compound that i cant push anymore")
                    return False
                
            '''
            while self.atoms.get(nextPos) is not None:
                nextPos = (nextPos[0] + move[0], nextPos[1] + move[1])
                if not self.inBoard(nextPos):
                    return False
            '''
        return True
    
    def handleMove(self, move):
        if not self.canMove(move, self.hero):
            return 
        self.handleCircles(move)
        self.handlePushes(move)
        self.hero.move(move)
        self.connectCompounds()
        
    def handleCircles(self, move):
        allCompounds = [self.hero] + self.compounds
        for pos, circle in self.circles.items():
            for compound in allCompounds:
                atom1, atom2 = compound.getCandidates(move, pos)
                if (atom1 != [] and atom2 != []):
                    if (circle.name == "green"):
                        compound.addConnection(atom1[0], atom2[0])
                    elif (circle.name == "red"):
                        compound.removeConnection(atom1[0], atom2[0])
                        isolatedCompound = compound.checkIsolation()
                        if isolatedCompound != []:
                            print("THERE IS A NEW COMPOUND!")
                            newCompound = Compound(isolatedCompound)
                            self.compounds.append(newCompound)
                            self.connectIsolatedCompounds()

                    elif (circle.name == "blue"):
                        return           
    
    def handlePushes(self, move):
        for atom in self.hero.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
          
            for compound in self.compounds:
                if compound.isInPosition(nextPos) and (len(self.hero.atoms) >= len(compound.atoms)) and self.canMove(move, compound):
                    compound.push(move)
        
    
    def connectIsolatedCompounds(self):
        allCompounds = self.compounds
        for i in range(len(allCompounds)-1):
            for j in range(i+1, len(allCompounds)):
                res = allCompounds[i].handleConnection(allCompounds[j])
                if res != []:
                    for tup in res:
                        tup[0].connect(tup[1], tup[2], tup[3])
                    res[0][0].atoms += res[0][1].atoms
                    self.compounds.remove(res[0][1])       
        
    
    def connectCompounds(self):
        allCompounds = [self.hero] + self.compounds
        for i in range(len(allCompounds)-1):
            for j in range(i+1, len(allCompounds)):
                res = allCompounds[i].handleConnection(allCompounds[j])
                if res != []: 
                    for tup in res:
                        tup[0].connect(tup[1], tup[2], tup[3])
                    res[0][0].atoms += res[0][1].atoms
                    self.compounds.remove(res[0][1])
        
    def drawBoard(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.walls:
                    pygame.draw.rect(surface, self.wallColor, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
                elif (x, y) not in self.blank:
                    pygame.draw.rect(surface, BACKGROUND, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
      
    def draw(self, surface):
        self.drawBoard(surface)

        for pos, circle in self.circles.items():
            circle.draw(surface, self.width, self.height, pos)

        self.hero.draw(surface, self.width, self.height)

        for compound in self.compounds:
            compound.draw(surface, self.width, self.height)
        
    def printStat(self):
        print("My hero is")
        for atom in self.hero.atoms:
            x = []
            for con in atom.connections:
                x.append(con.pos)
            print(atom.pos, x)
        print("=========")
        for i in self.compounds:
            l = []
            for a in i.atoms:
                l += [a.pos]
            print(l)
        print("=========")