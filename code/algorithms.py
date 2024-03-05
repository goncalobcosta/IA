from code.board import * 
import copy

class Algorithms:
    def __init__ (self, board):
        self.board = board

    @staticmethod
    def getNextBoards(board):
        nextBoards = []
        for move in DIRECTIONS:
            new_board = board.copy()
            new_board.handleMove(move)
            if new_board != board:
                nextBoards.append(new_board)
        return nextBoards

    @staticmethod
    def dfs (board, visited):
        print("olá")
        nextBoards = Algorithms.getNextBoards(board)
        print(nextBoards)
        visited.append(board)
        if board.win():
            print("Win")
            return

        for nextBoard in nextBoards:
            if nextBoard not in visited:
                print("visiting ", nextBoard.hero.atoms[0].pos)
                Algorithms.dfs(nextBoard, visited)


    
    