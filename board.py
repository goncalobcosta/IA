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
    
    def canPushCompound(self, compound, move):
        if len(self.hero.atoms) < len(compound.atoms):
            return False
        for atom in compound.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            if not self.inBoard(nextPos):
                return False
        return True
    
    def canMove(self, move):
        for atom in self.hero.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
            if not self.inBoard(nextPos):
                return False
            
            for compound in self.compounds:
                if compound.isInPosition(nextPos) and not self.canPushCompound(compound, move):
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
        if not self.canMove(move):
            return 
        print("I can move!")
        self.handlePushes(move)
        self.hero.move(move)
        self.connectCompounds()
        
        #self.handleCircles(move)
        
    
    def handlePushes(self, move):
        for atom in self.hero.atoms:
            pos = atom.pos
            nextPos = (pos[0] + move[0], pos[1] + move[1])
          
            for compound in self.compounds:
                if compound.isInPosition(nextPos) and self.canPushCompound(compound, move):
                    compound.push(move)
        
    
    def connectCompounds(self):
        allCompounds = [self.hero] + self.compounds
        for i in range(len(allCompounds)-1):
            for j in range(i+1, len(allCompounds)):
                res = allCompounds[i].handleConnection(allCompounds[j])
                if res is not None: 
                    res[0].connect(res[1], res[2], res[3])
                    self.compounds.remove(res[1])
        
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

        for compound in self.compounds:
            compound.draw(surface, self.width, self.height)
        
        self.hero.draw(surface, self.width, self.height)
        