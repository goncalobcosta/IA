import pygame

class Piece:
    def __init__(self, connections, x, y):
        self.x = x
        self.y = y
        self.connections = connections

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x*50.5, self.y*50.5, 45, 45))
