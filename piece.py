import pygame

class Piece:
    def __init__(self, connections, x, y):
        self.x = x
        self.y = y
        self.connections = connections


class Wall(Piece):
    def __init__(self, x, y):
        super().__init__(connections=0, x=x, y=y)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (239,175,26), (self.x*50.5, self.y*50.5, 45, 45))
    
class Hydrogen(Piece):
    def __init__(self, x, y):
        super().__init__(connections=1, x=x, y=y)
        self.image = pygame.transform.scale(pygame.image.load("atoms/hydrogen.png").convert_alpha(), (50, 50))
        
    def draw(self, surface):
        surface.blit(self.image, (self.x*50, self.y*50)) 
               
class Oxygen(Piece):
    def __init__(self, x, y):
        super().__init__(connections=2, x=x, y=y)
        self.image = pygame.transform.scale(pygame.image.load("atoms/oxygen.png").convert_alpha(), (50, 50))
        
    def draw(self, surface):
        surface.blit(self.image, (self.x*50, self.y*50)) 

class Nitrogen(Piece):
    def __init__(self, x, y):
        super().__init__(connections=3, x=x, y=y)
        self.image = pygame.transform.scale(pygame.image.load("atoms/nitrogen.png").convert_alpha(), (50, 50))

    def draw(self, surface):
        surface.blit(self.image, (self.x*50, self.y*50)) 
     
class Carbon(Piece):
    def __init__(self, x, y):
        super().__init__(connections=4, x=x, y=y)
        self.image = pygame.transform.scale(pygame.image.load("atoms/carbon.png").convert_alpha(), (50, 50))

    def draw(self, surface):
        surface.blit(self.image, (self.x*50, self.y*50)) 
    