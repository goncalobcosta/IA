import pygame
from atom import *
from circle import *

# DIRECTIONS
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

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
        
    def inBoard(self, pos):
        return (0 <= pos[0] < self.width and 0 <= pos[1] < self.height) and (pos not in self.blank) and (pos not in self.walls)
    
    def canPush(self, x, y, dx, dy):
        return self.grid[y+2*dy][x+2*dx] == None
    

    def canMove(self, move):
        for pos in self.compound.keys():
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            if not self.inBoard(nextPos):
                return False
            if self.atoms.get(nextPos) is not None:
                return False
        return True
    
    def handleMove(self, move):
        if not self.canMove(move):
            return 
        self.handleCircles(move)
        self.handlePushes(move)
        self.moveCompound(move)
        
    def handlePushes(self, move):
        for pos in self.compound.keys():
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            if self.atoms.get(nextPos) is not None:
                print(self.atoms[nextPos])

    def handleCircles(self, move):
        for pos, circle in self.circles.items():
            atom1, atom2 = self.getCandidates(pos, move)
            if (atom1 is not None and atom2 is not None):
                if (circle.name == "green"):
                    self.addConnection(atom1, atom2)
                '''
                elif (circle.name == "red"):
                    self.removeConnection(circle.pos, dx, dy)
                elif (circle.name == "blue"):
                    self.rotateCompound(circle.pos, dx, dy)
           '''
    
    def getCandidates(self, pos, move):
        x, y = pos 
        upLeft = self.compound.get((x, y))
        upRight = self.compound.get((x + 1, y))
        downLeft = self.compound.get((x, y + 1))
        downRight = self.compound.get((x + 1, y + 1))
       
        if move == UP:
            return downLeft, downRight
        elif move == DOWN:
            return upLeft, upRight
        elif move == LEFT:
            return upRight, downRight
        return upLeft, downLeft

    def addConnection(self, atom1, atom2):
        if atom1.connections > 0 and atom2.connections > 0:
            atom1.connections -= 1
            atom1.updateImage()
            atom2.connections -= 1
            atom2.updateImage()
    
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
      
        
    def pushAtoms(self, atoms, dx, dy):
        for atom in atoms:
            atom.move(dx, dy)
                
    def moveCompound(self, move):
        dx, dy = move
        updated_compound = {}  
        for pos, atom in self.compound.items():
            x, y = pos
            updated_pos = (x + dx, y + dy) 
            updated_compound[updated_pos] = atom  
        self.compound = updated_compound  
        self.connectAtoms()
            
    def connectAtom(self, connection):
        atom1, (pos2, atom2) = connection
        atom1.connections -= 1
        atom1.updateImage()
        atom2.connections -= 1
        atom2.updateImage()
        self.compound[pos2] = atom2
        self.atoms.pop(pos2)

    def isNextTo(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        if (x1 == x2 and abs(y1 - y2) == 1): return True
        if (y1 == y2 and abs(x1 - x2) == 1): return True
        return False

    def connectAtoms(self):
        connections = []
        for pos1, atom1 in self.compound.items():
            for pos2, atom2 in self.atoms.items():
                if self.isNextTo(pos1, pos2) and atom1.canConnectTo(atom2):
                    connections.append((atom1, (pos2, atom2)))
       
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

        for pos, circle in self.circles.items():
            circle.draw(surface, self.width, self.height, pos)

        for pos, atom in self.atoms.items():
            atom.draw(surface, self.width, self.height, pos)

        for pos, atom in self.compound.items():
            atom.draw(surface, self.width, self.height, pos)