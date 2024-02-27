import pygame
import sys
from board import Board
from hero import Hero
from piece import Piece, Wall, Carbon, Nitrogen, Hydrogen, Oxygen

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create game objects
board = Board(10, 8)
hero = Hero("hi", 1, 1)

running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero.move(0, -1)
            elif event.key == pygame.K_DOWN:
                hero.move(0, 1)
            elif event.key == pygame.K_LEFT:
                hero.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                hero.move(1, 0)

    # Draw game objects
    board.draw(screen)
    hero.draw(screen)
    wall = Wall(5, 5)
    wall.draw(screen)
    hydrogen = Hydrogen(6,5)
    hydrogen.draw(screen)
    
    oxygen = Oxygen(6,4)
    oxygen.draw(screen)
    
    nitrogen = Nitrogen(6,3)
    nitrogen.draw(screen)
    
    carbon = Carbon(6,2)
    carbon.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()