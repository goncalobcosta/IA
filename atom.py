import pygame

H = ("hydrogen", 1)
O = ("oxygen", 2)
N = ("nitrogen", 3)
C = ("carbon", 4)

class Atom:
    def __init__(self, atom, isHero = False):
        self.name, self.limitBound, = atom
        self.isHero = isHero  
        self.connections = self.limitBound
                
    def draw(self, surface, offX, offY):
        path = "resources/atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.connections) + ".png"
        image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        x, y = self.pos
        surface.blit(image, ((800 - offX * 50) // 2 + x*50, ((600 - offY * 50) // 2 + y*50)))
    
    def isConnectable(self):
        return self.connections < self.boundLimit