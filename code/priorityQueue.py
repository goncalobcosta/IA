import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, board):
        """
        Push an item into the priority queue.

        Parameters:
        - board: The item to be pushed into the queue.
        """
        heapq.heappush(self._queue, (board.cost + board.heuristic_estimate, board))

    def pop(self):
        """
        Pop and return the item with the highest priority from the priority queue.

        Returns:
        - The item with the highest priority.
        """
        return heapq.heappop(self._queue)[1]
    
    def empty(self):
        """
        Check if the priority queue is empty.

        Returns:
        - bool: True if the priority queue is empty, False otherwise.
        """
        return len(self._queue) == 0
    

    