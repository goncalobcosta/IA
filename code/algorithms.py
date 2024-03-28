from code.board import * 
from collections import deque
from code.priorityQueue import PriorityQueue

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

    @staticmethod
    def getNextBoards(board, visited):
        """
        Generate next possible boards from the current board.

        Parameters:
        - board (Board): The current board state.
        - visited (list): A list of visited board states.

        Returns:
        - nextBoards (list): A list of tuples containing the next possible board states along with their corresponding move directions.
        """
        nextBoards = []
        for move in DIRECTIONS:
            newBoard = board.copy()
            canMove = newBoard.handleMove(move)
            if canMove and newBoard not in visited:
                nextBoards.append((newBoard, DIR.get(move)))
        return nextBoards

    @staticmethod
    def dfs(board, visited, path, depth, limit):
        """
        Depth-first search algorithm to find a winning path on a game board.

        Parameters:
        - board (Board): The current board state.
        - visited (set): A set of visited board states. Defaults to an empty list.
        - path (list): The current path of moves. Defaults to an empty list.
        - depth (int): The current depth of the search. Defaults to 0.
        - limit (int): The maximum depth limit for the search. Defaults to 30.

        Returns:
        - path_to_win (list): A list of move directions leading to a winning state, or an empty list if no winning path is found within the limit.
        """
        nextBoards = Algorithms.getNextBoards(board, visited)        
        visited.add(board)

        if board.win():
            return path  
        
        if depth >= limit:
            return []

        for nextBoard, direction in nextBoards:
            path_to_win = Algorithms.dfs(nextBoard, visited, path + [direction], depth + 1, limit)
            if path_to_win:
                return path_to_win
        return []

    @staticmethod
    def bfs(board, limit):
        """
        Breadth-first search algorithm to find a winning path on a game board.

        Parameters:
        - board (Board): The initial board state.
        - limit (int): The maximum depth limit for the search.

        Returns:
        - path_to_win (list): A list of move directions leading to a winning state, or an empty list if no winning path is found within the limit.
        """
        visited = {board}
        queue = deque([(board, [])])

        while queue:
            current_board, path = queue.popleft()

            if current_board.win():
                return path

            if len(path) >= limit:
                continue

            nextBoards = Algorithms.getNextBoards(current_board, visited)

            for nextBoard, direction in nextBoards:
                queue.append((nextBoard, path + [direction]))
                visited.add(nextBoard)
            
        return []
        
    @staticmethod
    def greedyMove(board , nextBoards):
        """
        Selects the best move based on a greedy strategy for a given game board.

        Parameters:
        - board (Board): The current board state.
        - nextBoards (list): A list of tuples containing the next possible board states along with their corresponding move directions.

        Returns:
        - best (tuple): A tuple containing the best board state and its corresponding move direction.
        """
        bestValue = float('inf')        
        for b, direction in nextBoards:
            value = board.greedyMove(MOVE[direction])
            if value < bestValue:
                bestValue = value
                best = b, direction
        return best

    @staticmethod
    def bestFirst(board):
        """
        Best-first search algorithm to find a winning path on a game board.

        Parameters:
        - board (Board): The initial board state.

        Returns:
        - path_to_win (list): A list of move directions leading to a winning state, or an empty list if no winning path is found.
        """
        visited = set()
        path = []

        while True:
            if board.win(): 
                return path 
           
            visited.add(board)

            nextBoards = Algorithms.getNextBoards(board, visited)

            if nextBoards == []:
                return []

            nextBoard, direction = Algorithms.greedyMove(board, nextBoards)

            board = nextBoard
            path.append(direction)
                
    @staticmethod
    def greedySearch(board):
        """
        Greedy search algorithm to find a winning path on a game board.

        Parameters:
        - board (Board): The initial board state.

        Returns:
        - path_to_win (list): A list of move directions leading to a winning state, or an empty list if no winning path is found.
        """
        queue = PriorityQueue()
        visited = {board}
        
        board.cost = 0
        board.heuristic_estimate = 0
        board.path = []
        queue.push(board)
        
        while not queue.empty():
            currentBoard = queue.pop()    
            
            if currentBoard.win():
                return currentBoard.path
            
            nextBoards = Algorithms.getNextBoards(currentBoard, visited)
            for b, direction in nextBoards:
                visited.add(b)
                b.heuristic_estimate = currentBoard.greedyMove(MOVE[direction])
                b.cost = 0
                b.path = currentBoard.path + [direction]
                queue.push(b)
            
        return []
       
    @staticmethod
    def aStar(board):
        """
        A* search algorithm to find a winning path on a game board.

        Parameters:
        - board (Board): The initial board state.

        Returns:
        - path_to_win (list): A list of move directions leading to a winning state, or an empty list if no winning path is found.
        """
        queue = PriorityQueue()
        visited = {board}
        
        board.cost = 0
        board.heuristic_estimate = 0
        board.path = []
        queue.push(board)
                
        while not queue.empty():
            currentBoard = queue.pop()            
            
            if currentBoard.win():
                return currentBoard.path
            
            nextBoards = Algorithms.getNextBoards(currentBoard, visited)
            for b, direction in nextBoards:
                visited.add(b)
                b.heuristic_estimate = currentBoard.greedyMove(MOVE[direction]) + currentBoard.closestCircle(MOVE[direction]) * 0.1 
                b.cost = currentBoard.cost + 1
                b.path = currentBoard.path + [direction]
                queue.push(b)
        
        return []
     
  
     