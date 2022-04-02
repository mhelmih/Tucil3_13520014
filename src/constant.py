N = 4
""" Board Size (NxN). """

# Order: right, bottom, lelft, top
VER_DIR = [ 0, 1, 0, -1 ]
""" 
    Vertical Direction to move the empty block on the board. 
    +1 : Bottom
     0 : Nothing
    -1 : Top
"""

# Order: right, bottom, lelft, top
HOR_DIR = [ 1, 0, -1, 0 ]
""" 
    Horizontal Direction to move the empty block on the board. 
    +1 : Right
     0 : Nothing
    -1 : Left
"""

#: Goal state
GOAL_BOARD   = [[ 1,  2,  3,  4],
                [ 5,  6,  7,  8],
                [ 9, 10, 11, 12],
                [13, 14, 15, 16]]
""" 
    Final Board Arrangement. Block 16 is treated as an empty block.
"""
