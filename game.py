import pygame
import sys
from level import * 

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 138, 128)
YELLOW = (254, 216, 119)
BLUE = (166, 197, 254)
GREEN = (175, 219, 140)

board_start_x = (WIDTH - 9 * 50) // 2
board_start_y = (HEIGHT - 8 * 50) // 2


class Game:
    def __init__(self):
        pygame.init()
        self.state = "Menu"
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.titleFont = pygame.font.Font("resources/font/Quicksand-Medium.ttf", 100) 
        self.playFont = pygame.font.Font("resources/font/Quicksand-Regular.ttf", 30)
        self.option = 0
        
    def play(self):
        self.displayMenu()
        self.playGame()
    
    def drawMenu(self):
        self.screen.fill(WHITE)
        title = self.titleFont.render("SOKOBOND", True, GRAY)
        level1 = self.playFont.render("Level 1", True, BLACK)
        level2 = self.playFont.render("Level 2", True, BLACK)
        level3 = self.playFont.render("Level 3", True, BLACK)
        leave = self.playFont.render("Quit", True, BLACK)
  
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 30))
        level1_rect = level1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        level2_rect = level2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        level3_rect = level3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 110))
        leave_ret = leave.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 180))

        pygame.draw.rect(self.screen, BLUE, (350, 247 + self.option * 70, 105, 50))

        self.screen.blit(title, title_rect)
        self.screen.blit(level1, level1_rect)
        self.screen.blit(level2, level2_rect)
        self.screen.blit(level3, level3_rect)
        self.screen.blit(leave, leave_ret)

        pygame.display.flip()
    
    def displayMenu(self):
        self.screen.fill(WHITE)
        self.drawMenu()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.option = (self.option + 1) % 4
                        self.drawMenu()
                    elif event.key == pygame.K_UP:
                        self.option = (self.option - 1) % 4
                        self.drawMenu()
                    elif event.key == pygame.K_RETURN:
                        return
            pygame.display.flip()
            self.clock.tick(60)
    
    def playGame(self):
        self.board = Level(self.option).getLevelBoard()
        while (self.option != 3):
            self.screen.fill(WHITE)
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    break
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
        self.quit()
        
    def resetGame(self):
        self.board = Level(self.option).getLevelBoard()
        
    def quit(self):
        pygame.quit()
        sys.exit()
        
game = Game()
game.play()