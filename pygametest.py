import pygame
import sys
from board import Board
from hero import Hero
from piece import Piece, Wall, Carbon, Nitrogen, Hydrogen, Oxygen
#from easy import easy 

WIDTH = 800
HEIGHT = 800
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
board = Board(9, 8)

board.grid = [ ["X", Wall(1, 0), Wall(2, 0), Wall(3, 0), Wall(4, 0), Wall(5, 0), Wall(6, 0), Wall(7, 0), "X"],
              [Wall(0, 1), Wall(1, 1), None, None, None, None, None, Wall(7, 1), Wall(8, 1)],
              [Wall(0, 2), None, None, Hydrogen(3, 2), None, Hydrogen(5, 2), None, None, Wall(8, 2)],
              [Wall(0, 3), None, None, Wall(3, 3), None, Wall(5, 3), None, None, Wall(8, 3)],
              [Wall(0, 4), None, None, None, None, None, None, None, Wall(8, 4)],
              [Wall(0, 5), None, None, None, None, None, None, None, Wall(8, 5)],
              [Wall(0, 6), Wall(1, 6), Hydrogen(2, 6), None, None, None, Hydrogen(6, 6), Wall(7, 6), Wall(8, 6)],
              ["X", Wall(1, 7), Wall(2, 7), Wall(3, 7), Wall(4, 7), Wall(5, 7), Wall(6, 7), Wall(7, 7), "X"],
            ]

hero = Hero(4, 5)

running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and hero.canMove(0, -1, board):
                hero.move(0, -1)
            elif event.key == pygame.K_DOWN and hero.canMove(0, 1, board):
                hero.move(0, 1)
            elif event.key == pygame.K_LEFT and hero.canMove(-1, 0, board):
                hero.move(-1, 0)
            elif event.key == pygame.K_RIGHT and hero.canMove(1, 0, board):
                hero.move(1, 0)

    # Draw game objects
    board.draw(screen)
    hero.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()