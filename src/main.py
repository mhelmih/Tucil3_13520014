from os.path import exists
from Solver import Solver

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
            continue
        elif user_pick == "2":
            directory = "./test/"
            filename = input("Filename: ")
            if exists(directory + filename):
                with open(directory + filename, 'r') as f:
                    board = [[int(num) for num in line.split(' ')] for line in f if line.strip() != "" ]
            else:
                print(f"'{directory + filename}' is not exist.")
                continue
        print()
        
        puzzle = Solver(board)
        puzzle.solve()
        
    elif user_pick == "0":
        active = False
        print("Thank you!")
    else:
        print("Invalid Input.")
