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

def createBoard(width, height):
    arr = []
    for row in range(height):
        arr += [createOneRow(width)]
    return arr

def printBoard(A):
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width, height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(width, height):
    A = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            if 1 <= row <= height-1:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def randomCells(width, height):
    A = createBoard(width, height)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            A[row][col] = random.choice([0,1])

    return A

def copy(A):
    rows = len(A)
    cols = len(A[0])
    B = createBoard(rows, cols)
    for row in range(rows):
        for col in range(cols):
            B[row][col] = A[row][col]

    return B

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

