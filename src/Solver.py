import copy
import time
from PriorityQueue import PriorityQueue
from Node import Node
from constant import N, VER_DIR, HOR_DIR, GOAL_BOARD

class Solver:
    """ A class used to represent a solver of the 15-puzzle.
    
    Attributes
    ----------
    board_to_solve : list[list[int]]
        The board of 15-puzzle to be solved
    prio_queue : PriorityQueue
        The priority queue of Nodes to implement branch and bound algorithm
    total_x : int
        The value that determines if the board is solvable or not solvable.
    generated_nodes : int
        The counter for the generated Nodes
        
    Methods
    -------
    isSolvable(root_node)
        Calculate the value of total_x
    less(board_arr, i, i_idx)
        Count the number of blocks with number j such that j < i and idx_j > idx_i
    calculateEmptyPos(root_node)
        Return 1 if the empty block is at certain position and 0 if at the rest
    calculateCost(board)
        Calculate the cost needed for a board to go to the goal board.
    showBoard(board)
        Print the board
    showAllBoard(node)
        Print all boards recursively
    isIdxValid(idx)
        Check if idx is out of bounds
    solve()
        Perform the Branch and Bound Algorithm to solve the puzzle
    """
    
    def __init__(self, board_to_solve):
        """ 
        Parameters
        ---------
        board_to_solve : list[list[int]]
            The board of 15-puzzles to be solved
        """
        self.board_to_solve = board_to_solve
        self.prio_queue = PriorityQueue()
        self.total_x = 0
        self.generated_nodes = 0
        
    def isSolvable(self, root_node) -> bool:
        """ Calculate the value of total_x.
        
        total_x is sum of Less(i) + X where X is 1 if 
        the empty blocks is at certain position
        and 0 if at the rest.
        
        Parameters
        ----------
        root_node : Node
            The root node of a search space tree
            
        Returns
        -------
        boolean
            True if total_x is even, False if odd.
        """
        # store board numbers to a list
        board_numbers = []
        for i in range(N):
            for j in range(N):
                board_numbers.append(self.board_to_solve[i][j])
        
        # calculate and print Less(i)
        print("+----+----------+")
        print("|  i |  Less(i) |")
        print("+----+----------+")   
        total = 0
        for i in range(1, len(board_numbers) + 1):
            i_idx = 0
            for j in range(len(board_numbers)):
                if board_numbers[j] == i:
                    i_idx = j
                    
            less_i = self.less(board_numbers, i, i_idx)
            total += less_i
            
            if i < 10:
                print(f"|  {i} ", end="|    ")
            else:
                print(f"| {i} ", end="|    ")
                
            if less_i < 10:
                print(f" {less_i}    |")
            else:
                print(f"{less_i}    |")        
        print("+----+----------+")
        
        # determine empty value
        x = self.determineEmptyVal(root_node)
        self.total_x = total + x
        print(f"Total + X = {total} + {x} = {self.total_x}", end=" ")
        
        if self.total_x % 2 == 0:
            print("(Even)")
            return True
        else:
            print("(Odd)")
            return False
        
    def less(self, board_arr, i, i_idx) -> int:
        """ Count the number of blocks with number j such that j < i and idx_j > idx_i.
        
        Parameters
        ----------
        board_arr : list[int]
            The numbers in the board that stored in a list
        i : int
            The number to check
        i_idx : int
            The index of number i in board
        """
        count = 0
        for j in range(1, i):
            # in here, k is idx_j
            for k in range(len(board_arr)):
                if board_arr[k] == j and k > i_idx:
                    count += 1
        return count
    
    def determineEmptyVal(self, root_node) -> int:
        """ Determine the empty block value.
        
        Suppose the board size is 4x4. The empty block has value according 
        to its position on the board as follows: \n
        
        0 1 0 1\n
        1 0 1 0\n
        0 1 0 1\n
        1 0 1 0
        """
        i = root_node.empty_idx[0]
        j = root_node.empty_idx[1]
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            return 1
        else:
            return 0
                    
    def calculateCost(self, board) -> int:
        """ Calculate the cost needed for a board to go to the goal board. 
        
        The cost is calculated by how many blocks are out of place.
        """
        cost = 0
        for i in range(N):
            for j in range(N):
                if (board[i][j] != 16 and board[i][j] != GOAL_BOARD[i][j]):
                    cost += 1
        return cost
    
    def showBoard(self, board):
        """ Print the board. """
        for i in range(N):
            print("+-----+-----+-----+-----+")
            for j in range(N):
                if board[i][j] == 16:
                    print(f"|     ", end="")
                elif board[i][j] < 10:
                    print(f"|  {board[i][j]}  ", end="")
                else:
                    print(f"|  {board[i][j]} ", end="")
            print("|")
        print("+-----+-----+-----+-----+")

    def showAllBoard(self, node):
        """ Print the board recursively. """
        if node == None:
            return
        self.showAllBoard(node.parent)
        print(f"\nStep: {node.level}")
        self.showBoard(node.board)
        
    def isIdxValid(self, idx) -> bool:
        """ Check if idx is out of bounds. """
        return 0 <= idx[0] < N and 0 <= idx[1] < N
        
    def solve(self):
        """ Perform the Branch and Bound Algorithm to solve the puzzle. """
        print("\nInitial arrangement:")
        self.showBoard(self.board_to_solve)
        print()
        
        start_time = time.time() 
        
        # find the cost and empty block position to create the root node
        root_cost = self.calculateCost(self.board_to_solve)
        found = False
        i = 0
        while i < N and not found:
            j = 0;
            while j < N and not found:
                if self.board_to_solve[i][j] == 16:
                    found = True
                else:
                    j += 1
            if not found:
                i += 1
        root_empty_idx = [ i, j ]
        root_node = Node(None, self.board_to_solve, root_empty_idx, root_cost, 0)
        
        if not self.isSolvable(root_node):
            print("Sorry, this puzzle is not solvable.")
        else:
            print("This puzzle is solvable. Please wait.")
            last_time_checked = 0
            
            self.prio_queue.push(root_node)
            while not self.prio_queue.empty():
                minimum_node = self.prio_queue.pop()
                
                # check time if it goes too long
                time_check = round(time.time() - start_time) 
                if time_check != 0 and time_check != last_time_checked and time_check % 10 == 0:
                    print(f"{time_check} seconds have passed...")
                    last_time_checked = time_check
                
                # if cost == 0, then the node is the soltution
                if minimum_node.cost == 0:
                    self.showAllBoard(minimum_node)
                    print(f"Execution Time: {time.time() - start_time} s")
                    print(f"Generated Node(s): {self.generated_nodes} node(s)")
                    return
                
                # generate all possible child node(s)
                empty_idx_old = minimum_node.empty_idx
                for i in range(N):
                    empty_idx_new = [ empty_idx_old[0] + VER_DIR[i], empty_idx_old[1] + HOR_DIR[i] ] 
                                    
                    if self.isIdxValid(empty_idx_new):
                        self.generated_nodes += 1
                        
                        # deep copy so that the parent board wont be changed
                        child_board = copy.deepcopy(minimum_node.board)
                        
                        temp = child_board[empty_idx_old[0]][empty_idx_old[1]]
                        child_board[empty_idx_old[0]][empty_idx_old[1]] = child_board[empty_idx_new[0]][empty_idx_new[1]]
                        child_board[empty_idx_new[0]][empty_idx_new[1]] = temp
                        
                        child_cost = self.calculateCost(child_board)
                        child_node = Node(minimum_node, child_board, empty_idx_new, child_cost, minimum_node.level + 1)

                        self.prio_queue.push(child_node)
