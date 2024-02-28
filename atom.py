import pygame

class Atom:
    def __init__(self, name, pos, isHero = False):
        self.name = name
        self.pos = pos
        self.isHero = isHero  
        if (name == "hydrogen"):
            self.connections = 1
        elif (name == "carbon"):
            self.connections = 4
        elif (name == "nitrogen"):
            self.connections = 3
        elif (name == "oxygen"):
            self.connections = 2

    def move(self, dx, dy):
        x, y = self.pos
        self.pos = (x+dx, y+dy)

    def draw(self, surface):
        path = "atoms/" + self.name + "/" + ("hero" if self.isHero else self.name) + str(self.connections) + ".png"
        image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (50, 50))
        x, y = self.pos
        surface.blit(image, ((800 - 9 * 50) // 2 + x*50, ((800 - 8 * 50) // 2 + y*50)))

    def canConnectTo(self, atom):
        if self.connections == 0 or atom.connections > self.connections:
            return False
        x, y = self.pos
        xx, yy = atom.pos
        if y == yy and abs(x - xx) == 1:
            return True
        if x == xx and abs(y - yy) == 1:
            return True
        return False