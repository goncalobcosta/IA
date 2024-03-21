import os
import pygame
import sys
from code.level import * 
from code.algorithms import *
import random
import math 

os.environ['SDL_AUDIODRIVER'] = 'dsp'

LEVELS = 0
ABOUT = 1
QUIT = 2

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.titleFont = pygame.font.Font("resources/fonts/Quicksand-Medium.ttf", 80) 
        self.playFont = pygame.font.Font("resources/fonts/Quicksand-Medium.ttf", 30)
        self.nameFont = pygame.font.Font("resources/fonts/Quicksand-Regular.ttf", 40)
        self.levelFont = pygame.font.Font("resources/fonts/Quicksand-Medium.ttf", 50)
        self.commandFont = pygame.font.Font("resources/fonts/Quicksand-Regular.ttf", 20)
        self.option = 0
        self.stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(50)]
    

    def play(self):
        while True: 
            self.displayMenu()
           
    def drawLevels(self):
        self.screen.fill(WHITE)

        menu = self.commandFont.render("<- Menu [M]", True, DARK_GRAY)
        menu_rect = menu.get_rect(topleft=(20, 20))

        title = self.titleFont.render("Levels", True, GRAY)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        self.screen.blit(menu, menu_rect)
        self.screen.blit(title, title_rect)

        pygame.draw.rect(self.screen, BLUE, (150 + (self.level % 5) * 110, 270 + (self.level // 5) * 110, 70, 70))

        for row in range(2):
            for col in range(5):
                level_num = row * 5 + col + 1
                level_rect = pygame.Rect(col * 110 + 150, row * 110 + 270, 70, 70)
                pygame.draw.rect(self.screen, GRAY, level_rect, 2)  
                level_text = self.levelFont.render(str(level_num), True, DARK_GRAY)
                text_rect = level_text.get_rect(center=level_rect.center)
                self.screen.blit(level_text, text_rect)

        pygame.display.flip()

        pygame.display.flip()

    def displayLevels(self):
        self.level = 0
        self.drawLevels()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.level = (self.level + 5) % 10
                        self.drawLevels()
                    elif event.key == pygame.K_UP:
                        self.level = (self.level - 5) % 10
                        self.drawLevels()
                    elif event.key == pygame.K_LEFT:
                        self.level = (self.level - 1) % 10
                        self.drawLevels()
                    elif event.key == pygame.K_RIGHT:
                        self.level = (self.level + 1) % 10
                        self.drawLevels()
                    elif event.key == pygame.K_m:
                        self.displayMenu()
                        self.quit()
                    elif event.key == pygame.K_RETURN:
                        self.playGame()
                        return
            pygame.display.flip()
            self.clock.tick(60)

    def drawMenu(self):
        self.screen.fill(WHITE)
        title = self.titleFont.render("SOKOBOND", True, GRAY)
        play = self.playFont.render("play", True, BLACK)
        about = self.playFont.render("about", True, BLACK)
        leave = self.playFont.render("quit", True, BLACK)
  
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        play_rect = play.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        about_rect = about.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        leave_ret = leave.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 170))

        pygame.draw.rect(self.screen, BLUE, (350, 308 + self.option * 70, 105, 50))

        self.screen.blit(title, title_rect)
        self.screen.blit(play, play_rect)
        self.screen.blit(about, about_rect)
        self.screen.blit(leave, leave_ret)

        pygame.display.flip()
    
    def drawAbout(self):
        self.screen.fill(WHITE)

        title = self.titleFont.render("SOKOBOND", True, GRAY)
        line1 = self.playFont.render("Sokobond is an elegantly designed puzzle game", True, BLACK)
        line2 = self.playFont.render("about chemistry. It's logical, minimalist, and beautiful", True, BLACK)
        line3 = self.playFont.render("crafted with love, science and chemistry!.", True, BLACK)
        back = self.playFont.render("< back >", True, BLACK)
    
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 70))
        line1_rect = line1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        line2_rect = line2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
        line3_rect = line3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
        back_ret = back.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 170))

        pygame.draw.rect(self.screen, BLUE, (330, 447, 140, 50))

        self.screen.blit(title, title_rect)
        self.screen.blit(line1, line1_rect)
        self.screen.blit(line2, line2_rect)
        self.screen.blit(line3, line3_rect)
        self.screen.blit(back, back_ret)

        pygame.display.flip()

    def displayAbout(self):
        self.drawAbout()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.displayMenu()
                        return
            pygame.display.flip()
            self.clock.tick(60)
    
    def drawStars(self):
        for star in self.stars:
            self.draw_star(self.screen, GOLD, star, 5, 10, 5)  # Adjust the parameters as needed

    def updateStars(self):
        for i in range(len(self.stars)):
            self.stars[i] = (self.stars[i][0] + random.randint(-2, 2), self.stars[i][1] + random.randint(-2, 2))

    def draw_star(self, surface, color, pos, outer_radius, inner_radius, points):
        x, y = pos
        angle = 0
        angle_increment = math.pi * 2 / points
        outer_points = []

        for _ in range(points):
            outer_points.extend([(x + outer_radius * math.cos(angle), y + outer_radius * math.sin(angle))])
            angle += angle_increment
            outer_points.extend([(x + inner_radius * math.cos(angle), y + inner_radius * math.sin(angle))])
            angle += angle_increment

        pygame.draw.circle(surface, GOLD, (x, y), int(inner_radius * 0.6))  # Adjust the factor for the center size
        pygame.draw.polygon(surface, color, outer_points, 0)

    def drawWin(self):
        self.screen.fill(WHITE)
        self.board.draw(self.screen)

        title = self.titleFont.render("You Won!", True, GOLD)
        back = self.playFont.render("Play Another", True, BLACK)
        
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 145))
        back_ret = back.get_rect(center=(WIDTH // 2, HEIGHT // 10 * 9 ))

        self.drawStars() 

        pygame.draw.rect(self.screen, BLUE, (287.5, HEIGHT // 10 * 9 - 30, 220, 65))

        self.screen.blit(title, title_rect)
        self.screen.blit(back, back_ret)

        pygame.display.flip()

    def displayWin(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Play another
                        self.displayMenu()
                        return

            self.drawWin()
            self.updateStars()  # Update star positions
            pygame.display.flip()
            self.clock.tick(60)

    def displayMenu(self):
        self.drawMenu()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.option = (self.option + 1) % 3
                        self.drawMenu()
                    elif event.key == pygame.K_UP:
                        self.option = (self.option - 1) % 3
                        self.drawMenu()
                    elif event.key == pygame.K_RETURN:
                        if (self.option == LEVELS): 
                            self.displayLevels()
                            return
                        elif (self.option == ABOUT): 
                            self.displayAbout()
                            return
                        else : 
                            self.quit()
                            return
            pygame.display.flip()
            self.clock.tick(60)
    
    

    def playGame(self):

        
        self.board = Level(self.level).board

        while (True):

            if self.board.win() : 
                self.displayWin()

            self.screen.fill(WHITE)
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.quit()
                        break
                    elif event.key == pygame.K_m:
                        self.play()
                        self.quit()
                        break
                    elif event.key == pygame.K_l:
                        self.displayLevels()
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
                    elif event.key == pygame.K_e:
                        self.board.printStat()

            self.board.draw(self.screen)
            self.drawCommands(self.board.name)
            
            pygame.display.flip()
            self.clock.tick(60)        
        
    def drawCommands(self, name):
        reset = self.commandFont.render("R : reset", True, DARK_GRAY)
        hint = self.commandFont.render("H : hint", True, DARK_GRAY)
        levels = self.commandFont.render("L : levels", True, DARK_GRAY)
        menu = self.commandFont.render("M : menu", True, DARK_GRAY)
        leave = self.commandFont.render("Q : quit", True, DARK_GRAY)
        name = self.nameFont.render(name, True, DARK_GRAY)

        reset_rect = reset.get_rect(topleft=(20, 20))
        hint_rect = hint.get_rect(topleft=(20, 45))
        levels_rect = levels.get_rect(topleft=(20, 70))
        menu_rect = menu.get_rect(topleft=(20, 95))
        leave_rect = leave.get_rect(topleft=(20, 120))
        name_rect = name.get_rect(bottomleft=(20, 580))
        
        self.screen.blit(reset, reset_rect)
        self.screen.blit(levels, levels_rect)
        self.screen.blit(menu, menu_rect)
        self.screen.blit(hint, hint_rect)
        self.screen.blit(leave, leave_rect)
        self.screen.blit(name, name_rect)
        
    def resetGame(self):
        self.board = Level(self.level).board
        
    def quit(self):
        pygame.quit()
        sys.exit()