import pygame

He = ("helium", 0)
H = ("hydrogen", 1)
O = ("oxygen", 2)
N = ("nitrogen", 3)
C = ("carbon", 4)

WIDTH = 800
HEIGHT = 600
SQUARE = 50

# DIRECTIONS
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


class Atom:
    def __init__(self, atom, pos, isHero = False):
        self.name, self.boundLimit, = atom
        self.pos = pos
        self.connections = []
        self.isHero = isHero  
        self.visited = False
        path = "resources/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.boundLimit - len(self.connections)) + ".png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))

    def draw(self, surface, offX, offY):
        x, y = self.pos
        surface.blit(self.image, ((WIDTH - offX * SQUARE) // 2 + x*SQUARE, ((HEIGHT - offY * SQUARE) // 2 + y*SQUARE)))
    
    def updateImage(self):
        path = "resources/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.boundLimit - len(self.connections)) + ".png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        
    def connect(self, atom):
        self.connections.append(atom)
        self.updateImage()
    
    def disconnect(self, atom):
        self.connections.remove(atom)
        self.updateImage()
    
    def move(self, move):
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
    
    def isInPosition(self, pos):
        return self.pos == pos
    
    def isNextTo(self, atom):
        x1, y1 = self.pos
        x2, y2 = atom.pos
        if (x1 == x2 and abs(y1 - y2) == 1): return True
        if (y1 == y2 and abs(x1 - x2) == 1): return True
        return False
    
    def canConnectTo(self, atom):
        return self.isNextTo(atom) and len(self.connections) < self.boundLimit and len(atom.connections) < atom.boundLimit
        
    def drawConnection(self, surface, offX, offY, atom, doubleConnection):
        direction = (atom.pos[0] - self.pos[0], atom.pos[1] - self.pos[1])
        if (doubleConnection):
            if direction == UP:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 17, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 5, 50))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 27, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 5, 50))
            elif direction == DOWN:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 17, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 5, 50))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 27, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 5, 50))
            elif direction == LEFT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 17), 50, 5))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 27), 50, 5))
            elif direction == RIGHT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 17), 50, 5))
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 27), 50, 5))
        else:
            if direction == UP:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 5, 50))
            elif direction == DOWN:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 5, 50))
            elif direction == LEFT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + atom.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + atom.pos[1]*SQUARE + 22), 50, 5))
            elif direction == RIGHT:
                pygame.draw.rect(surface, (0,0,0), ((WIDTH - offX * SQUARE) // 2 + self.pos[0]*SQUARE + 22, ((HEIGHT - offY * SQUARE) // 2 + self.pos[1]*SQUARE + 22), 50, 5))
