import copy
import time

from PriorityQueue import PriorityQueue
from Node import Node
from constant import N, VER_DIR, HOR_DIR, GOAL_BOARD

class Solver:
    def __init__(self, board_to_solve):
        self.board_to_solve = board_to_solve
        self.prio_queue = PriorityQueue()
        self.generated_nodes = 0
        
    def isSolvable(self, root_node) -> bool:
        total = 0
        board_numbers = []
        for i in range(N):
            for j in range(N):
                board_numbers.append(self.board_to_solve[i][j])
        
        print("+----+----------+")
        print("|  i |  Less(i) |")
        print("+----+----------+")   
        
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
        x = self.findEmptyPos(root_node)
        print(f"Total + X = {total} + {x} = {total+x}", end=" ")
        if (total+x) % 2 == 0:
            print("(Even)")
            return True
        else:
            print("(Odd)")
            return False
        
                    
    def less(self, board_arr, i, i_idx) -> int:
        count = 0
        for j in range(1, i):
            for k in range(len(board_arr)):
                if board_arr[k] == j and k > i_idx:
                    count += 1
        return count
    
    def findEmptyPos(self, root_node) -> int:
        i = root_node.empty_idx[0]
        j = root_node.empty_idx[1]
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            return 1
        else:
            return 0
                    
    def calculateCost(self, board) -> int:
        cost = 0
        for i in range(N):
            for j in range(N):
                if (board[i][j] != 16 and board[i][j] != GOAL_BOARD[i][j]):
                    cost += 1
        return cost
    
    def showBoard(self, board):
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
        if node == None:
            return
        self.showAllBoard(node.parent)
        print(f"Step: {node.level}")
        self.showBoard(node.board)
        print()
        
    def isIdxValid(self, x, y) -> bool:
        return 0 <= x < N and 0 <= y < N
        
    def solve(self):
        print("Initial arrangement:")
        self.showBoard(self.board_to_solve)
        print()
        
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
        start_time = time.time()
        if not self.isSolvable(root_node):
            print("Sorry, this puzzle is not solvable.")
            print(f"Execution Time : {time.time() - start_time} s")
            print(f"Generated Nodes: {self.generated_nodes} node(s)")
        else:
            print("This puzzle is solvable. Please wait.\n")
            self.prio_queue.push(root_node)
            while not self.prio_queue.empty():
                minimum_node = self.prio_queue.pop()
                if minimum_node.cost == 0:
                    self.showAllBoard(minimum_node)
                    print(f"Execution Time : {time.time() - start_time}")
                    print(f"Generated Nodes: {self.generated_nodes}")
                    return
                
                empty_idx_old = minimum_node.empty_idx
                for i in range(N):
                    empty_idx_new = [ empty_idx_old[0] + VER_DIR[i], empty_idx_old[1] + HOR_DIR[i] ] 
                                    
                    if self.isIdxValid(empty_idx_new[0], empty_idx_new[1]):
                        self.generated_nodes += 1
                        child_board = copy.deepcopy(minimum_node.board)
                        
                        temp = child_board[empty_idx_old[0]][empty_idx_old[1]]
                        child_board[empty_idx_old[0]][empty_idx_old[1]] = child_board[empty_idx_new[0]][empty_idx_new[1]]
                        child_board[empty_idx_new[0]][empty_idx_new[1]] = temp
                        
                        child_cost = self.calculateCost(child_board)
                        child_node = Node(minimum_node, child_board, empty_idx_new, child_cost, minimum_node.level + 1)

                        self.prio_queue.push(child_node)
