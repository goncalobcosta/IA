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


grid = [["X", "W", "W", "W", "W", "W", "W", "W", "X"],
        ["W", "W", None, None, None, None, None, "W", "W"],
        ["W", None, None, None, None, None, None, None, "W"],
        ["W", None, None, "W", None, "W", None, None, "W"],
        ["W", None, None, None, None, None, None, None, "W"],
        ["W", None, None, None, None, None, None, None, "W"],
        ["W", "W", None, None, None, None, None, "W", "W"],
        ["X", "W", "W", "W", "W", "W", "W", "W", "X"]
        ]

atoms = [Atom("hydrogen", (3, 2)), Atom("hydrogen", (5, 2)), Atom("hydrogen", (2, 6)), Atom("hydrogen", (6, 6))]
compound = [Atom("carbon", (4, 5), True)]

# Create game objects
board = Board(9, 8, grid, atoms, compound)


global board_start_x
global board_start_y
board_start_x = (WIDTH - board.width * 50) // 2
board_start_y = (HEIGHT - board.height * 50) // 2


class Game:
    def __init__(self, board):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = board

    def play(self):
        while (True):
            self.screen.fill(WHITE)
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == pygame.K_q:
                        self.resetGame()
                    elif event.key == pygame.K_UP :
                        self.board.handleMove(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.board.handleMove(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.board.handleMove(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.board.handleMove(1, 0)

            # Draw game objects
            self.board.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def resetGame(self):
        self.board = Board(9, 8, [["X", "W", "W", "W", "W", "W", "W", "W", "X"],
        ["W", "W", None, None, None, None, None, "W", "W"],
        ["W", None, None, None, None, None, None, None, "W"],
        ["W", None, None, "W", None, "W", None, None, "W"],
        ["W", None, None, None, None, None, None, None, "W"],
        ["W", None, None, None, None, None, None, None, "W"],
        ["W", "W", None, None, None, None, None, "W", "W"],
        ["X", "W", "W", "W", "W", "W", "W", "W", "X"]
        ], [Atom("hydrogen", (3, 2)), Atom("hydrogen", (5, 2)), Atom("hydrogen", (2, 6)), Atom("hydrogen", (6, 6))], [Atom("carbon", (4, 5), True)])
        
    def quit(self):
        pygame.quit()
        sys.exit()
        
game = Game(board)
game.play()