import pygame
from atom import *

global board_start_x
global board_start_y


class Board:
    def __init__(self, width, height, grid, atoms, compound, wallColor):
        self.width = width
        self.height = height
        self.grid = grid
        self.atoms = atoms
        self.compound = compound 
        self.wallColor = wallColor
    
    def inBoard(self, x, y):
        return (0 <= x < self.width and 0 <= y < self.height) and self.grid[y][x] == None
    
    def canPush(self, x, y, dx, dy):
        return self.grid[y+2*dy][x+2*dx] == None
    
    def nextToAtom(self, x, y):
        return any(atom.pos == (x,y) for atom in self.atoms)
    
    def handleMove(self, dx, dy):
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
    
    def drawBoard(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == "X":
                    continue 
                elif self.grid[y][x] == "W":
                    pygame.draw.rect(surface, self.wallColor, ((800 - self.width * 50) // 2 + x*50, (600 - self.height * 50) // 2 + y*50, 46, 46))
                    continue
                pygame.draw.rect(surface, (243, 243, 243), ((800 - self.width * 50) // 2 + x*50, (600 - self.height * 50) // 2 + y*50, 46, 46))
                   
    def draw(self, surface):
        self.drawBoard(surface)
        
        for atom in self.atoms:
            atom.draw(surface, self.width, self.height)
        
        for atom in self.compound:
            atom.draw(surface, self.width, self.height)
                