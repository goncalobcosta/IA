import pygame

class Hero:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)

    def set_position(self, x, y):
        self.position = (x, y)

    def move(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0]*50, self.position[1]*50, 50, 50))
