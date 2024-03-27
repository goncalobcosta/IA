import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, board):
        heapq.heappush(self._queue, (board.cost + board.heuristic_estimate, board))

    def pop(self):
        return heapq.heappop(self._queue)[1]
    
    def empty(self):
        return len(self._queue) == 0
    

    