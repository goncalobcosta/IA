import pygame
from atom import *

global board_start_x
global board_start_y

COR_BRANCA = (255, 255, 255)
COR_CINZENTA = (243, 243, 243)

class Board:
    def __init__(self, width, height, grid, compound):
        self.width = width
        self.height = height
        self.grid = grid
        self.compound = compound #[(4,5), (2,6)]
  
    def inBoard(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def checkarroundAtoms(self):
        new_atoms = []
        print(self.compound)
        for (x, y) in self.compound:
            if self.grid[y][x].connections > 0:
                if self.inBoard(x, y - 1) and isinstance(self.grid[y - 1][x], Atom) and (x, y - 1) not in self.compound and self.grid[y - 1][x].connections > 0:
                    new_atoms.append((x, y - 1))
                    self.grid[y - 1][x].connections -= 1
                    self.grid[y][x].connections -= 1
                    self.grid[y - 1][x].isConnected = True
                    self.grid[y][x].isConnected = True
                if self.inBoard(x, y + 1) and isinstance(self.grid[y + 1][x], Atom) and (x, y + 1) not in self.compound and self.grid[y + 1][x].connections > 0:
                    new_atoms.append((x, y + 1))
                    self.grid[y + 1][x].connections -= 1
                    self.grid[y][x].connections -= 1
                    self.grid[y + 1][x].isConnected = True
                    self.grid[y][x].isConnected = True
                if self.inBoard(x - 1, y) and isinstance(self.grid[y][x - 1], Atom) and (x - 1, y) not in self.compound and self.grid[y][x - 1].connections > 0:
                    new_atoms.append((x - 1, y))
                    self.grid[y][x - 1].connections -= 1
                    self.grid[y][x].connections -= 1
                    self.grid[y][x - 1].isConnected = True
                    self.grid[y][x].isConnected = True
                if self.inBoard(x + 1, y) and isinstance(self.grid[y][x + 1], Atom) and (x + 1, y) not in self.compound and self.grid[y][x + 1].connections > 0:
                    new_atoms.append((x + 1, y))
                    self.grid[y][x + 1].connections -= 1
                    self.grid[y][x].connections -= 1
                    self.grid[y][x + 1].isConnected = True
                    self.grid[y][x].isConnected = True

        self.compound = self.compound + new_atoms

    def canMove(self, dx, dy):
        for (x, y) in self.compound:
            if not self.inBoard(x+dx, y+dy):
                return False
            if self.grid[y+dy][x+dx] == None:
                continue
            if self.grid[y+dy][x+dx] == "W" or self.grid[y+dy][x+dx] == "X" :
                return False
            if not self.grid[y+dy][x+dx].isConnected:
                return False
        return True

    def moveCompound(self, dx, dy):
        l = []
        for (x, y) in self.compound:
            self.grid[y][x], self.grid[y + dy][x + dx] = None, self.grid[y][x]
            l.append((x+dx, y+dy))
        self.compound = l
        print(self.compound)
        self.checkarroundAtoms()

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == "X":
                    continue 
                elif self.grid[y][x] == "W":
                    pygame.draw.rect(surface, (239,175,26), ((800 - 9 * 50) // 2 + x*50, (800 - 8 * 50) // 2 + y*50, 46, 46))
                    continue
                pygame.draw.rect(surface, COR_CINZENTA, ((800 - self.width * 50) // 2 + x*50, (800 - self.height * 50) // 2 + y*50, 46, 46))
                if self.grid[y][x] != None:
                    self.grid[y][x].draw(surface, x, y)
        
                    
