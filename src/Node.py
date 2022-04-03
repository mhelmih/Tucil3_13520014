class Node:
    """ A class used to represent a node of a tree.
    
    Attributes
    ----------
    parent : Node
        The parent node
    board : list[list[int]]
        The board of the node
    empty_idx : list[int]
        The index where the empty block is located on the board
    cost : int
        The cost needed to reach this node
    level : int
        The depth level of the node
        
    Methods
    -------
    __lt__(other)
        For comparison purpose. Used in priority queue
    """
    
    def __init__(self, parent, board, empty_idx, cost, level):
        """ 
        Parameters
        ----------
        parent : Node
            The parent node
        board : list[list[int]]
            The board of the node
        empty_idx : list[int]
            The index where the empty block is located on the board
        cost : int
            The cost needed to reach this node
        level : int
            The depth level of the node
        """
        self.parent = parent
        self.board = board
        self.empty_idx = empty_idx
        self.cost = cost
        self.level = level

    def __lt__(self, other) -> bool:
        """ Compare this node with other node, returns True if this node is "less" than other node. """
        return self.cost + self.level < other.cost + other.level
