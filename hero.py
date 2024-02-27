import pygame

class Hero:
    def __init__(self, x, y):
        self.pieces = []
        self.x = x
        self.y = y 
        self.image = pygame.transform.smoothscale(pygame.image.load("atoms/hero.png").convert_alpha(), (50, 50))

    def move(self, x, y):
        self.x += x 
        self.y += y
        
    def canMove(self, dir_x, dir_y, board):
        return board.isEmpty(self.x + dir_x, self.y + dir_y)
            
    def draw(self, surface):
        surface.blit(self.image, ((800 - 9 * 50) // 2 + self.x*50, (800 - 8 * 50) // 2 + self.y*50, 46, 46))
