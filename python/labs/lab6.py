'''
Created on Jacob Gerega
@author:   10/8/19
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
import math
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1
    pass  # TODO

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    binaryString = ""
    while n != 0:
        binaryNumber = n % 2
        binaryString = str(binaryNumber) + binaryString
        n = n // 2
    return binaryString
    pass  # TODO

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    decimalNumber = 0
    indexCounter = 0
    binaryNumberAsInteger = int(s)
    while binaryNumberAsInteger != 0:
        decimalNumber += ((binaryNumberAsInteger % 10) * (math.pow(2, indexCounter)))
        binaryNumberAsInteger = binaryNumberAsInteger // 10
        indexCounter = indexCounter + 1
    return int(decimalNumber)
    pass  # TODO

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    stringLength = 8
    decimalNumber = binaryToNum(s)
    decimalNumber = decimalNumber + 1
    incrementedBinaryString = numToBinary(decimalNumber)
    eightBitBinaryString = ""
    eightBitBinaryString += ((stringLength-len(incrementedBinaryString))*'0') + incrementedBinaryString
    if len(eightBitBinaryString) > 8:
        return "00000000"
    return eightBitBinaryString
    pass  # TODO

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    counter = 0
    binaryString = s
    while counter <= n:
        print(binaryString)
        binaryString = increment(binaryString)
        counter = counter + 1
    pass  # TODO

#the ternary representation of 59 is 24 because like binary, you just keep getting the remainder when dividing it by the base of the number and further computing the number

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    ternaryString = ""
    while n != 0:
        binaryNumber = n % 3
        ternaryString = str(binaryNumber) + ternaryString
        n = n // 3
    return ternaryString
    pass  # TODO

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    decimalNumber = 0
    indexCounter = 0
    ternaryNumberAsInteger = int(s)
    while ternaryNumberAsInteger != 0:
        decimalNumber += ((ternaryNumberAsInteger % 10) * (math.pow(3, indexCounter)))
        ternaryNumberAsInteger = ternaryNumberAsInteger // 10
        indexCounter = indexCounter + 1
    return int(decimalNumber)
    pass  # TODO