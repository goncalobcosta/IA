from code.algorithms import Algorithms
from code.game import Game
from code.board import *
from code.level import Level
import time


def main():    
    '''
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
        
        path = Algorithms.dfs(board, set(), [], 0, 30)
        res += str(len(path)) + " | "
                    
        path = Algorithms.bfs(board, 30)
        res += str(len(path)) + " | "
                
        path = Algorithms.bestFirst(board)
        res += str(len(path)) + " | "
                   
        path = Algorithms.greedySearch(board)
        res += str(len(path)) + " | "
                    
        path = Algorithms.aStar(board)
        res += str(len(path)) + " | "
        print(res)


if __name__ == "__main__":
    main()