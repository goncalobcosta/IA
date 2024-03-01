import pygame
import sys
from level import * 


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.titleFont = pygame.font.Font("resources/font/Quicksand-Medium.ttf", 100) 
        self.playFont = pygame.font.Font("resources/font/Quicksand-Regular.ttf", 30)
        self.commandFont = pygame.font.Font("resources/font/Quicksand-Regular.ttf", 20)
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
        while (True):
            self.screen.fill(WHITE)
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.quit()
                        break
                    elif event.key == pygame.K_m:
                        self.play()
                        self.quit()
                        break
                    elif event.key == pygame.K_r:
                        self.resetGame()
                    elif event.key == pygame.K_UP :
                        self.board.handleMove(UP)
                    elif event.key == pygame.K_DOWN:
                        self.board.handleMove(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.board.handleMove(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.board.handleMove(RIGHT)

            # Draw game objects
            self.board.draw(self.screen)
            self.drawCommands()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        
    def drawCommands(self):
        reset = self.commandFont.render("R : reset", True, DARK_GRAY)
        menu = self.commandFont.render("M : menu", True, DARK_GRAY)
        hint = self.commandFont.render("H : hint", True, DARK_GRAY)
        leave = self.commandFont.render("L : leave", True, DARK_GRAY)
        
        reset_rect = reset.get_rect(topleft=(20, 20))
        menu_rect = menu.get_rect(topleft=(20, 45))
        hint_rect = hint.get_rect(topleft=(20, 70))
        leave_rect = leave.get_rect(topleft=(20, 95))
        
        self.screen.blit(reset, reset_rect)
        self.screen.blit(menu, menu_rect)
        self.screen.blit(hint, hint_rect)
        self.screen.blit(leave, leave_rect)
        
    def resetGame(self):
        self.board = Level(self.option).getLevelBoard()
        
    def quit(self):
        pygame.quit()
        sys.exit()


game = Game()
game.play()

'''
import time

def if_elifs(value):
    if value == 1:
        return "One"
    elif value == 2:
        return "Two"
    elif value == 3:
        return "Three"
    elif value == 4:
        return "Four"
    elif value == 5:
        return "Five"
    else:
        return "Other"

def match_case(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
        case _:
            return "Other"

# Timing if-elifs
start_time = time.time()
for i in range(1000000):
    result = if_elifs(i % 7)
end_time = time.time()
if_elifs_time = end_time - start_time

# Timing match-case
start_time = time.time()
for i in range(1000000):
    result = match_case(i % 7)
end_time = time.time()
match_case_time = end_time - start_time

print("Time taken for if-elifs:", if_elifs_time)
print("Time taken for match-case:", match_case_time)
'''