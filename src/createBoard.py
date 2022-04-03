import random
import copy
from os.path import exists
from constant import N, GOAL_BOARD, VER_DIR, HOR_DIR

def from_file() -> list[list[int]]:
    """ Read from a file then return the matrix inside it. """
    
    board = []
    directory = "./test/"
    filename = input("Filename: ")
    
    if not exists(directory + filename):
        print(f"'{directory + filename}' is not exist.")
        return []
    else:    
        with open(directory + filename, 'r') as f:
            board = [[int(num) for num in line.split(' ')] for line in f if line.strip() != "" ]
        
        return board
        

def from_random() -> list[list[int]]:
    """ Randomize the goal board according to the user choice of difficulty then return the matrix. """
    
    board = copy.deepcopy(GOAL_BOARD)
    
    print("[1] Easy")
    print("[2] Medium")
    print("[3] Hard")
    user_choice = input("Pick difficulty: ")
    if user_choice == "1":
        difficulty = 10
    elif user_choice == "2":
        difficulty = 15
    elif user_choice == "3":
        difficulty = 20
    else:
        print("Invalid Input.")
        return []
    
    empty_idx = [ 3, 3 ]
    previous_idx = [ 3, 3 ]
    # the more the difficulty, the more the empty block moved
    for _ in range(difficulty):
        # find valid moves
        valid_moves = []
        for j in range(N):
            empty_idx_new = [ empty_idx[0] + VER_DIR[j], empty_idx[1] + HOR_DIR[j] ]
            if 0 <= empty_idx_new[0] < N and 0 <= empty_idx_new[1] < N:
                valid_moves.append(empty_idx_new)
        
        # pick random new move, last move wont be picked again
        random_move = valid_moves[random.randint(0, len(valid_moves) - 1)]
        while random_move == previous_idx:
            random_move = valid_moves[random.randint(0, len(valid_moves) - 1)]
        
        # swap
        temp = board[empty_idx[0]][empty_idx[1]]
        board[empty_idx[0]][empty_idx[1]] = board[random_move[0]][random_move[1]]
        board[random_move[0]][random_move[1]] = temp
        
        # update empty_idx so that there is no back and forth movement
        previous_idx = empty_idx
        empty_idx = random_move
        
        
    return board