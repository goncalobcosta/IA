import pygame

class Atom:
    def __init__(self, name, isHero = False):
        self.name = name
        self.isHero = isHero
        self.isConnected = False 
        if (name == "hydrogen"):
            self.connections = 1
        elif (name == "carbon"):
            self.connections = 4
        elif (name == "nitrogen"):
            self.connections = 3
        elif (name == "oxygen"):
            self.connections = 2

    def draw(self, surface, x, y):
        path = "atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.connections) + ".png"
        image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        surface.blit(image, ((800 - 9 * 50) // 2 + x*50, ((800 - 8 * 50) // 2 + y*50)))

    