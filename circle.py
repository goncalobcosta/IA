import pygame
from atom import *

BREAK = "red"
ADD = "green"
ROTATE = "blue"

class Circle:
    def __init__(self, name):
        self.name = name
        path = "circles/" + name + "_circle.png"
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (18, 18))

    def draw(self, surface, offX, offY, pos):
        x, y = pos
        if self.name == "red":
            surface.blit(self.image, ((800 - offX * 50) // 2 + x*50 + 39, (600 - offY * 50) // 2 + y*50 + 39))
        if self.name == "blue":
            surface.blit(self.image, ((800 - offX * 50) // 2 + x*50 + 41.5, (600 - offY * 50) // 2 + y*50 + 41.5))
        if self.name == "green":
            surface.blit(self.image, ((800 - offX * 50) // 2 + x*50 + 41, (600 - offY * 50) // 2 + y*50 + 41))
