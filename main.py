from code.algorithms import Algorithms
from code.game import Game
from code.board import *
from code.level import Level
import time


def main():    
    
    game = Game()
    game.play()
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    

    print("State Space explored")
    print("| Level | DFS | BFS | Best-First | Greedy | A* |")
    print("| --- | --- | --- | --- | --- | --- |")
    for i in range(10):
        board = Level(i).board
        res = "| " + str(i+1) + " | "        
        
        s = time.time()
        Algorithms.dfs(board, [], [], 0, 30)
        e = time.time()
        
        res += str(e-s) + " | "

        s1 = time.time()
        Algorithms.bfs(board)
        e1 = time.time()
        res += str(e1-s1) + " | "
       
        s2 = time.time()  
        Algorithms.bestFirst(board)
        e2 = time.time()
        res += str(e2-s2) + " | "
        
        s3 = time.time()  
        Algorithms.greedySearch(board)
        e3 = time.time()
        res += str(e3-s3) + " | "
         
        s4 = time.time()     
        Algorithms.aStar(board)
        e4 = time.time()
        res += str(e4-s4) + " | "
        print(res)
    '''

if __name__ == "__main__":
    main()