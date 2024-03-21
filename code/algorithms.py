from code.board import * 
from collections import deque

DIR = {
    (0, -1) :  "UP" ,
    (0, 1) : "DOWN" ,
    (-1, 0) : "LEFT",
    (1, 0) : "RIGHT", 
}

class Algorithms:
    def __init__ (self, board):
        self.board = board

    @staticmethod
    def getNextBoards(board):
        nextBoards = []
        for move in DIRECTIONS:
            new_board = board.copy()
            canMove = new_board.handleMove(move)
            if canMove:
                nextBoards.append((new_board, DIR.get(move)))
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