import pygame


H = ("hydrogen", 1)
O = ("oxygen", 2)
N = ("nitrogen", 3)
C = ("carbon", 4)

WIDTH = 800
HEIGHT = 600
SQUARE = 50

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
        
    def addConnection(self, atom):
        self.connections.append(atom)
    
    def isInPosition(self, pos):
        return self.pos == pos
    
    
    
    
    
    
    
    def canAddConnection(self):
        return self.connections < self.boundLimit
    
    def canConnectTo(self, atom):
        return self.connections > 0 and atom.connections > 0
