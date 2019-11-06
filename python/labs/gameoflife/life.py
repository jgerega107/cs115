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

