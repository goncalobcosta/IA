import pygame
import sys
from board import Board
from atom import *


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

grid = [ ["X", "W", "W", "W", "W", "W", "W", "W", "X"],
              ["W", "W", None, None, None, None, None, "W", "W"],
              ["W", None, None, Atom("hydrogen"), None, Atom("hydrogen"), None, None, "W"],
              ["W", None, None, "W", None, "W", None, None, "W"],
              ["W", None, None, None, None, None, None, None, "W"],
              ["W", None, None, None, Atom("carbon", True), None, None, None, "W"],
              ["W", "W", Atom("hydrogen"), None, None, None, Atom("hydrogen"), "W", "W"],
              ["X", "W", "W", "W", "W", "W", "W", "W", "X"]
            ]


# Create game objects
board = Board(9, 8, grid, [(4, 5)])



global board_start_x
global board_start_y
board_start_x = (WIDTH - board.width * 50) // 2
board_start_y = (HEIGHT - board.height * 50) // 2

running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and board.canMove(0, -1):
                board.moveCompound(0, -1)
            elif event.key == pygame.K_DOWN and board.canMove(0, 1):
                board.moveCompound(0, 1)
            elif event.key == pygame.K_LEFT and board.canMove(-1, 0):
                board.moveCompound(-1, 0)
            elif event.key == pygame.K_RIGHT and board.canMove( 1, 0):
                board.moveCompound(1, 0)

    # Draw game objects
    board.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()