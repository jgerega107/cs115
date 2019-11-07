#
# life.py - Game of Life lab
#
# Name:
# Pledge:
#

import sys, random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

#createBoard: takes in a width and height, returns a 2D array of zeros
def createBoard(width, height):
    arr = []
    for row in range(height):
        arr += [createOneRow(width)]
    return arr

#printBoard: takes in a 2D array board and prints it correctly instead of one line
def printBoard(A):
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

#diagonalize: takes in a width and a height and returns a board with ones going diagonally through it
def diagonalize(width, height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

#innerCells: takes in a width and a height and returns a board filled with ones except the outer border.
def innerCells(width, height):
    A = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if 1 <= row <= height-1:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

#randomCells: takes in a width and a height and returns a board filled randomly with ones while still staying inside the border
def randomCells(width, height):
    A = createBoard(width, height)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            A[row][col] = random.choice([0,1])

    return A

#copy: takes in a said board and constructs a said board based on same specifications and contents without making the new board a memory reference to the older board.
def copy(A):
    rows = len(A)
    cols = len(A[0])
    B = createBoard(rows, cols)
    for row in range(rows):
        for col in range(cols):
            B[row][col] = A[row][col]

    return B

#innerReverse: takes in a board and reverses the contents while still acknowledging the border
def innerReverse(A):
    rows = len(A)
    cols = len(A[0])
    B = copy(A)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if B[row][col] == 1:
                B[row][col] = 0
            else:
                B[row][col] = 1

    return B

#next_life_generation: takes in a board and brings the said board to the next generation of life according to the given rules for life and death
def next_life_generation(A):
    rows = len(A)
    cols = len(A[0])
    B = copy(A)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if B[row][col] == 1:
                if countNeighbors(row, col, A) < 2 or countNeighbors(row, col, A) > 3:
                    B[row][col] = 0
                else:
                    B[row][col] = 1
            else:
                if countNeighbors(row, col, A) == 3:
                    B[row][col] = 1
                else:
                    B[row][col] = 0
    return B

#countNeighbors: helper method for next_life_generation, counts how many live neighbors are around a given cell
def countNeighbors(row, col, A):
    liveNeighbors = 0
    #left and right
    if A[row+1][col] == 1:
        liveNeighbors+=1
    if A[row-1][col] == 1:
        liveNeighbors+=1
    #corners
    if A[row-1][col-1] == 1:
        liveNeighbors += 1
    if A[row+1][col+1] == 1:
        liveNeighbors += 1
    if A[row+1][col-1] == 1:
        liveNeighbors += 1
    if A[row-1][col+1] == 1:
        liveNeighbors += 1
    #above and below
    if A[row][col+1] == 1:
        liveNeighbors += 1
    if A[row][col-1] == 1:
        liveNeighbors += 1
    return liveNeighbors