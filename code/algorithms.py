from code.board import * 
from copy import copy

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
                nextBoards.append(new_board)
        return nextBoards

    @staticmethod
    def dfs(board, visited, path=[], depth=0, limit=30):

        nextBoards = Algorithms.getNextBoards(board)        
        visited.append(board)

        if board.win():
            return path  
        
        if depth >= limit:
            return None

        for nextBoard in nextBoards:
            if nextBoard not in visited:
                path_to_win = Algorithms.dfs(nextBoard, visited, path + [nextBoard.hero.atoms[0].pos], depth + 1, limit)
                if path_to_win:
                    return path_to_win
        return None

    @staticmethod
    def convert_to_directions(path):
        directions = []

        for i in range(1, len(path)):
            current_pos = path[i - 1]
            next_pos = path[i]

            if current_pos[0] < next_pos[0]:
                directions.append("RIGHT")
            elif current_pos[0] > next_pos[0]:
                directions.append("LEFT")
            elif current_pos[1] < next_pos[1]:
                directions.append("DOWN")
            elif current_pos[1] > next_pos[1]:
                directions.append("UP")

        return directions
