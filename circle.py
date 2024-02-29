import pygame

class Circle:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.image = "circles/" + name + "_circle.png"
        
    def draw(self, surface, offX, offY):
        x, y = self.pos
        if self.name == "red":
            image = pygame.transform.smoothscale(pygame.image.load(self.image).convert_alpha(), (18, 18))
            surface.blit(image, ((800 - offX * 50) // 2 + x*50 + 39, (800 - offY * 50) // 2 + y*50 + 39))
        if self.name == "blue":
            image = pygame.transform.smoothscale(pygame.image.load(self.image).convert_alpha(), (13, 13))
            surface.blit(image, ((800 - offX * 50) // 2 + x*50 + 41.5, (800 - offY * 50) // 2 + y*50 + 41.5))
        if self.name == "green":
            image = pygame.transform.smoothscale(pygame.image.load(self.image).convert_alpha(), (14, 14))
            surface.blit(image, ((800 - offX * 50) // 2 + x*50 + 41, (800 - offY * 50) // 2 + y*50 + 41))
