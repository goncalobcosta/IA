import os
import pygame
import sys
import time
import random
import math 
from code.level import * 
from code.algorithms import *

os.environ['SDL_AUDIODRIVER'] = 'dsp'

LEVELS = 0
EXTRA = 1
ABOUT = 2
QUIT = 3

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
        self.offset = 0

    def play(self):
        """
        Main game loop.
        """
        while True: 
            self.displayMenu()
           
    def drawLevels(self):
        """
        Draw the levels menu.
        """
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

    def drawMenu(self):
        """
        Draw the main menu.
        """
        self.screen.fill(WHITE)
        title = self.titleFont.render("SOKOBOND", True, GRAY)
        play = self.playFont.render("play", True, BLACK)
        extra = self.playFont.render("extra", True, BLACK)
        about = self.playFont.render("about", True, BLACK)
        leave = self.playFont.render("quit", True, BLACK)
  
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 30))
        play_rect = play.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        extra_rect = extra.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
        about_rect = about.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
        leave_ret = leave.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 210))

        pygame.draw.rect(self.screen, BLUE, (350, 278 + self.option * 70, 105, 50))

        self.screen.blit(title, title_rect)
        self.screen.blit(play, play_rect)
        self.screen.blit(extra, extra_rect)
        self.screen.blit(about, about_rect)
        self.screen.blit(leave, leave_ret)

        pygame.display.flip()
    
    def drawAbout(self):
        """
        Draw the about page.
        """
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
 
    def drawStars(self):
        """
        Draw stars.
        """
        for star in self.stars:
            self.drawStar(self.screen, GOLD, star, 5, 10, 5) 

    def updateStars(self):
        """
        Update stars.
        """
        for i in range(len(self.stars)):
            self.stars[i] = (self.stars[i][0] + random.randint(-2, 2), self.stars[i][1] + random.randint(-2, 2))

    def drawStar(self, surface, color, pos, outer_radius, inner_radius, points):
        """
        Draw a star.
        """
        x, y = pos
        angle = 0
        angle_increment = math.pi * 2 / points
        outer_points = []

        for _ in range(points):
            outer_points.extend([(x + outer_radius * math.cos(angle), y + outer_radius * math.sin(angle))])
            angle += angle_increment
            outer_points.extend([(x + inner_radius * math.cos(angle), y + inner_radius * math.sin(angle))])
            angle += angle_increment

        pygame.draw.circle(surface, GOLD, (x, y), int(inner_radius * 0.6)) 
        pygame.draw.polygon(surface, color, outer_points, 0)

    def drawHint(self, move):
        """
        Draw a hint.
        """        
        title = self.titleFont.render(move, True, GOLD)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 145))
        self.screen.blit(title, title_rect)

    def drawWin(self):
        """
        Draw the win menu.
        """
        self.screen.fill(WHITE)
        self.board.draw(self.screen)

        title = self.titleFont.render("You Won!", True, GOLD)
        back = self.playFont.render("Level menu", True, BLACK)
        again = self.playFont.render("Play again", True, BLACK)
        
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 145))
        back_ret = back.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 10 * 9 ))
        again_ret = again.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 10 * 9 ))

        self.drawStars() 

        pygame.draw.rect(self.screen, BLUE, (137.5 + 300 * self.winOption, HEIGHT // 10 * 9 - 30, 220, 65))

        self.screen.blit(title, title_rect)
        self.screen.blit(back, back_ret)
        self.screen.blit(again, again_ret)

        pygame.display.flip()

    def drawCommands(self, name):
        """
        Draw the command menu on the screen.
        """
        reset = self.commandFont.render("R : reset", True, DARK_GRAY)
        hint = self.commandFont.render("H : hint", True, DARK_GRAY)
        levels = self.commandFont.render("L : levels", True, DARK_GRAY)
        menu = self.commandFont.render("M : menu", True, DARK_GRAY)
        leave = self.commandFont.render("Q : quit", True, DARK_GRAY)
        name = self.nameFont.render(name, True, DARK_GRAY)

        dfs = self.commandFont.render("1 : DFS", True, DARK_GRAY)
        bfs = self.commandFont.render("2 : BFS", True, DARK_GRAY)
        greedy = self.commandFont.render("3 : Best First", True, DARK_GRAY)
        heuristic = self.commandFont.render("4 : Greedy", True, DARK_GRAY)
        aStar = self.commandFont.render("5 : A*", True, DARK_GRAY)

        reset_rect = reset.get_rect(topleft=(20, 20))
        hint_rect = hint.get_rect(topleft=(20, 45))
        levels_rect = levels.get_rect(topleft=(20, 70))
        menu_rect = menu.get_rect(topleft=(20, 95))
        leave_rect = leave.get_rect(topleft=(20, 120))
        name_rect = name.get_rect(bottomleft=(20, 580))
        
        dfs_rect = dfs.get_rect(bottomleft=(250, 565))
        bfs_rect = bfs.get_rect(bottomleft=(350, 565))
        greedy_rect = greedy.get_rect(bottomleft=(440, 565))
        heuristic_rect = heuristic.get_rect(bottomleft=(580, 565))
        aStar_rect = aStar.get_rect(bottomleft=(700, 565))
        
        self.screen.blit(reset, reset_rect)
        self.screen.blit(levels, levels_rect)
        self.screen.blit(menu, menu_rect)
        self.screen.blit(hint, hint_rect)
        self.screen.blit(leave, leave_rect)
        self.screen.blit(name, name_rect)
        
        self.screen.blit(dfs, dfs_rect)
        self.screen.blit(bfs, bfs_rect)
        self.screen.blit(greedy, greedy_rect)
        self.screen.blit(heuristic, heuristic_rect)
        self.screen.blit(aStar, aStar_rect)
        
    def displayAbout(self):
        """
        Display the about page and handle user input.
        """
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
    
    def displayLevels(self):
        """
        Display the levels menu and handle user input for level selection.
        """
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
                    elif event.key == pygame.K_UP:
                        self.level = (self.level - 5) % 10
                    elif event.key == pygame.K_LEFT:
                        self.level = (self.level - 1) % 10
                    elif event.key == pygame.K_RIGHT:
                        self.level = (self.level + 1) % 10
                    elif event.key == pygame.K_m:
                        self.displayMenu()
                        self.quit()
                    elif event.key == pygame.K_RETURN:
                        self.playGame()
                        return
            self.drawLevels()
            pygame.display.flip()

            self.clock.tick(60)

    def displayWin(self):
        """
        Display the win menu and handle user input.
        """
        self.winOption = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                        self.winOption = (self.winOption + 1) % 2
                    elif event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                        self.winOption = (self.winOption - 1) % 2                  
                    if event.key == pygame.K_RETURN:
                        if self.winOption == 0:
                            self.playGame()
                        else:
                            self.displayLevels()
                        return
            self.drawWin()
            self.updateStars() 
            pygame.display.flip()
            self.clock.tick(60)

    def displayMenu(self):
        """
        Display the main menu and handle user input.
        """
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
                        if (self.option == LEVELS): 
                            self.offset = 0
                            self.displayLevels()
                            return
                        if (self.option == EXTRA): 
                            self.offset = 10
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
       
    def solve(self, path):
        """
        Solve the level with the given path.
        """
        if path == []:
            self.useHint = True
            return
        for move in path:
            time.sleep(0.5)
            self.board.handleMove(MOVE[move])
            self.screen.fill(WHITE)
            self.board.draw(self.screen)
            self.drawCommands(self.board.name)
            pygame.display.flip()
        self.displayWin()
        self.quit()
    
    def resetGame(self):
        """
        Reset the game by loading the initial state of the current level.
        """
        self.board = Level(self.level).board
        
    def playGame(self):
        """
        Start playing the game.
        """
        self.board = Level(self.level + self.offset).board
        self.useHint = False
        
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
                    elif event.key == pygame.K_l:
                        self.displayLevels()
                        self.quit()
                        break
                    elif event.key == pygame.K_m:
                        self.play()
                        self.quit()
                        break
                    elif event.key == pygame.K_r:
                        self.resetGame()
                    elif event.key == pygame.K_h:
                        path = Algorithms.aStar(self.board)
                        self.useHint = True
                    elif event.key == pygame.K_1:
                        print("DFS search")
                        path = Algorithms.dfs(self.board, [], [], 0, 30)
                        print(path)
                        self.solve(path)
                    elif event.key == pygame.K_2:
                        print("BFS search")
                        path = Algorithms.bfs(self.board, 30)
                        print(path)
                        self.solve(path)
                    elif event.key == pygame.K_3:
                        print("Best first search")
                        path = Algorithms.bestFirst(self.board)
                        print(path)
                        self.solve(path)
                    elif event.key == pygame.K_4:
                        print("Greedy algorithm")
                        path = Algorithms.greedySearch(self.board)
                        print(path)
                        self.solve(path)
                    elif event.key == pygame.K_5:
                        print("A* algorithm")
                        path = Algorithms.aStar(self.board)
                        print(path)
                        self.solve(path)
                    elif event.key == pygame.K_UP :
                        self.board.handleMove(UP)
                    elif event.key == pygame.K_DOWN:
                        self.useHint = False
                        self.board.handleMove(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.useHint = False
                        self.board.handleMove(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.useHint = False
                        self.board.handleMove(RIGHT)

            self.board.draw(self.screen)
            self.drawCommands(self.board.name)
            if self.useHint: 
                text = 'No solution' if path == [] else path[0]
                self.drawHint(text)
            pygame.display.flip()
            self.clock.tick(60)     
            
    def quit(self):
        """
        Quit the game.
        """
        pygame.quit()
        sys.exit()