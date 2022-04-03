from Solver import Solver
from createBoard import from_file, from_random

print(" _ ___     ___            _       ___      _             ")
print("/ | __|___| _ \\_  _ _____| |___  / __| ___| |_ _____ _ _ ")
print("| |__ \\___|  _/ || |_ /_ / / -_) \\__ \\/ _ \\ \\ V / -_) '_|")
print("|_|___/   |_|  \\_,_/__/__|_\\___| |___/\\___/_|\\_/\\___|_|  ")

active = True
while active:
    print()
    print("="*57)
    print()
    print("       +----------------------------------------+")
    print("       | Initial Board Arrangement Input Method |")
    print("       +----------------------------------------+")
    print("       | [1] Random Number                      |")
    print("       | [2] Text File                          |")
    print("       |                                        |")
    print("       | [0] Exit                               |")
    print("       +----------------------------------------+")
    print()
    user_pick = input("Pick input method: ")
    
    if user_pick == "1" or user_pick == "2":
        if user_pick == "1":
            board = from_random()
        elif user_pick == "2":
            board = from_file()
        
        if board != []:
            puzzle = Solver(board)
            puzzle.solve()
        
    elif user_pick == "0":
        active = False
        print("Thank you!")
    else:
        print("Invalid Input.")
