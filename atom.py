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

    def draw(self, surface, offX, offY, pos):
        path = "resources/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.connections) + ".png"
        image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        x, y = pos
        surface.blit(image, ((WIDTH - offX * SQUARE) // 2 + x*SQUARE, ((HEIGHT - offY * SQUARE) // 2 + y*SQUARE)))
    
    def isConnectable(self):
        return self.connections < self.boundLimit