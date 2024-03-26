from code.board import * 
from collections import deque

DIR = {
    (0, -1) : "UP",
    (0, 1) : "DOWN",
    (-1, 0) : "LEFT",
    (1, 0) : "RIGHT", 
}

MOVE = {
    "UP" : (0, -1),
    "DOWN" : (0, 1) ,
    "LEFT" : (-1, 0) ,
    "RIGHT" : (1, 0) , 
}

class Algorithms:
    def __init__ (self, board):
        self.board = board

    @staticmethod
    def getNextBoards(board, visited=[]):
        nextBoards = []
        for move in DIRECTIONS:
            newBoard = board.copy()
            canMove = newBoard.handleMove(move)
            if canMove and newBoard not in visited:
                nextBoards.append((newBoard, DIR.get(move)))
        return nextBoards

    @staticmethod
    def dfs(board, visited=[], path=[], depth=0, limit=30):

        nextBoards = Algorithms.getNextBoards(board)        
        visited.append(board)

        if board.win():
            return path  
        
        if depth >= limit:
            return None

        for nextBoard, direction in nextBoards:
            if nextBoard not in visited:
                path_to_win = Algorithms.dfs(nextBoard, visited, path + [direction], depth + 1, limit)
                if path_to_win:
                    return path_to_win
        return None

    @staticmethod
    def bfs(board, limit=30):
        visited = []
        queue = deque([(board, [])])

        while queue:
            current_board, path = queue.popleft()
            visited.append(current_board)

            if current_board.win():
                return path

            if len(path) >= limit:
                continue

            nextBoards = Algorithms.getNextBoards(current_board)

            for nextBoard, direction in nextBoards:
                if nextBoard not in visited:
                    queue.append((nextBoard, path + [direction]))
                    visited.append(nextBoard)

        return None
    
    @staticmethod
    def greedy(board):
        
        visited = []
        path = []

        while True:
            if board.win():
                return path 
           
            visited.append(board)

            nextBoards = Algorithms.getNextBoards(board, visited)

            if nextBoards == []:
                print("Impossible to win")
                print(path)
                return []

            nextBoard, direction = Algorithms.greedyMove(board, nextBoards)

            board = nextBoard
            path.append(direction)
            
            

                
    @staticmethod
    def greedyMove(board, nextBoards):
        bestValue = float('inf')
        for b, direction in nextBoards:
            value = board.greedyMove(MOVE[direction])
            if value < bestValue:
                bestValue = value
                best = b, direction
        return best
        
    @staticmethod
    def aStar(board):
        return
        
        
     