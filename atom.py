import pygame

H = ("hydrogen", 1)
O = ("oxygen", 2)
N = ("nitrogen", 3)
C = ("carbon", 4)

WIDTH = 800
HEIGHT = 600
SQUARE = 50

class Atom:
    def __init__(self, atom, isHero = False):
        self.name, self.limitBound, = atom
        self.isHero = isHero  
        self.connections = self.limitBound
        path = "resources/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.connections) + ".png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        

    def draw(self, surface, offX, offY, pos):
        x, y = pos
        surface.blit(self.image, ((WIDTH - offX * SQUARE) // 2 + x*SQUARE, ((HEIGHT - offY * SQUARE) // 2 + y*SQUARE)))
    
    def canAddConnection(self):
        return self.connections < self.boundLimit
    
    def canConnectTo(self, atom):
        return self.connections > 0 and atom.connections > 0

    def updateImage(self):
        path = "resources/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.connections) + ".png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        