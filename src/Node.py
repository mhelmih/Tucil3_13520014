class Node:
    def __init__(self, parent, board, empty_idx, cost, level):  
        self.parent = parent
        self.board = board
        self.empty_idx = empty_idx
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost
