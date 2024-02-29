import pygame
from atom import *
from circle import *

# Screen Size
WIDTH = 800
HEIGHT = 600
SQUARE = 50

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
    def __init__(self, width, height, walls, blank, atoms, compound, circles, wallColor):
        self.width = width
        self.height = height
        self.walls = walls
        self.blank = blank
        self.atoms = atoms
        self.compound = compound 
        self.circles = circles
        self.wallColor = wallColor
        
    def inBoard(self, x, y):
        return (0 <= x < self.width and 0 <= y < self.height) and self.grid[y][x] == None
    
    def canPush(self, x, y, dx, dy):
        return self.grid[y+2*dy][x+2*dx] == None
    
    def nextToAtom(self, x, y):
        return any(atom.pos == (x,y) for atom in self.atoms)
    
    def handleMove(self, dx, dy):
        
        self.checkCircles(dx, dy)
        ll = [(atom.name, atom.pos) for atom in self.atoms]
        ll2 = [(atom.name, atom.pos) for atom in self.compound]
        print(ll)
        print(ll2)

        atomsToPush = []
        for atom in self.compound:
            x, y = atom.pos
            if not self.inBoard(x+dx, y+dy):
                return
            if self.nextToAtom(x+dx, y+dy) :
                if not self.canPush(x, y, dx, dy):
                    return 
                atomsToPush += [atom for atom in self.atoms if atom.pos == (x+dx, y+dy)]
                
        self.pushAtoms(atomsToPush, dx, dy)    
        self.moveCompound(dx, dy)
        
    def checkCircles(self, dx, dy):
        for circle in self.circles:
            if (circle.name == "green"):
                self.addConnection(circle.pos, dx, dy)
            if (circle.name == "red"):
                self.removeConnection(circle.pos, dx, dy)
            if (circle.name == "blue"):
                self.rotateCompound(circle.pos, dx, dy)
           
    def addConnection(self, pos, dx, dy):
        x, y = pos 
        candidates = []
        if dx == 0 and dy == -1:
            candidates = [(x, y + 1), (x + 1, y + 1)]
        if dx == 0 and dy == 1:
            candidates = [(x, y), (x + 1, y)]
        if dx == -1 and dy == 0:
            candidates = [(x + 1, y + 1), (x + 1, y)]
        if dx == 1 and dy == 0:
            candidates = [(x, y), (x, y + 1)]
        
        l = [atom for atom in self.compound if atom.pos in candidates]

        if len(l) == 2 and l[0].connections > 0 and l[1].connections > 0:
            self.doubleConnect(l[1], l[0])

    def removeConnection(self, pos, dx, dy):
        x, y = pos 
        candidates = []
        if dx == 0 and dy == -1:
            candidates = [(x, y + 1), (x + 1, y + 1)]
        if dx == 0 and dy == 1:
            candidates = [(x, y), (x + 1, y)]
        if dx == -1 and dy == 0:
            candidates = [(x + 1, y + 1), (x + 1, y)]
        if dx == 1 and dy == 0:
            candidates = [(x, y), (x, y + 1)]
        
        l = [atom for atom in self.compound if atom.pos in candidates]

        if len(l) == 2 and l[1].notFull() and l[0].notFull():
            self.removeAtom(l[1], l[0])
    
    def rotateCompound(self, pos, dx, dy):
        x, y = pos 
        candidates = []
        if dx == 0 and dy == -1:
            candidates = [(x, y + 1), (x + 1, y + 1)]
        if dx == 0 and dy == 1:
            candidates = [(x, y), (x + 1, y)]
        if dx == -1 and dy == 0:
            candidates = [(x + 1, y + 1), (x + 1, y)]
        if dx == 1 and dy == 0:
            candidates = [(x, y), (x, y + 1)]
        
        l = [atom for atom in self.compound if atom.pos in candidates]

        if len(l) == 2:
            self.rotateAtom(l[1], l[0], dx, dy)
        
    def doubleConnect(self, atom, atom2):
        atom.connections -= 1
        atom2.connections -= 1
        
    def pushAtoms(self, atoms, dx, dy):
        for atom in atoms:
            atom.move(dx, dy)
                
    def moveCompound(self, dx, dy):
        for atom in self.compound:
            atom.move(dx, dy)
        self.connectAtoms()
            
    def connectAtom(self, connection):
        atom1, atom2 = connection
        atom1.connections -= 1
        atom2.connections -= 1
        self.compound.append(atom2)
        self.atoms.remove(atom2)
    
    def connectAtoms(self):
        connections = []
        for atom in self.compound:
            for single in self.atoms:
                if atom.canConnectTo(single):
                    connections.append((atom, single))
       
        for connection in connections:
            self.connectAtom(connection)

    def removeAtom(self, atom1, atom2):

        if (atom1.connections == 0): 
            self.atoms.append(atom1)
            self.compound.remove(atom1)
        if (atom2.connections == 0): 
            self.atoms.append(atom2)
            self.compound.remove(atom2)
        atom1.connections += 1
        atom2.connections += 1
    
    def rotateAtom(self, atom1, atom2, dx, dy):
        (x1, y1) = atom1.pos
        (x2, y2) = atom2.pos
        
        if dx == 0 and dy == -1: #cima
            if (x1 < x2): 
                atom2.move(-1, 1)
            else: 
                atom1.move(-1, 1)
        if dx == 0 and dy == 1: #baixo
            if (x1 < x2): 
                atom1.move(1, -1)
            else: 
                atom2.move(1, -1)
        if dx == -1 and dy == 0: #esquerda
            if (y1 < y2): 
                atom1.move(1, 1)
            else: 
                atom2.move(1, 1)
        if dx == 1 and dy == 0: #direita
            if (y1 < y2): 
                atom2.move(-1, -1)  
            else: 
                atom1.move(-1, -1)  

    def drawBoard(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.walls:
                    pygame.draw.rect(surface, self.wallColor, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
                elif (x, y) not in self.blank:
                    pygame.draw.rect(surface, BACKGROUND, ((WIDTH - self.width * SQUARE) // 2 + x*SQUARE, (HEIGHT - self.height * SQUARE) // 2 + y*SQUARE, 46, 46))
      
    def draw(self, surface):
        self.drawBoard(surface)
        
        