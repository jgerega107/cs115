from cs115 import map,reduce
import math

'''
Created on 10/15/19
@author:   Jacob Gerega and Kevin
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def compress(s): 
    binaryList = map(numToBinary, countRepeat(s, "0", 0))
    bitCompliantList = map(fillBits, binaryList)
    return reduce(lambda x,y: x+y, bitCompliantList)

def countRepeat(s, z, n):
    if not s:
        return [n]
    elif n == MAX_RUN_LENGTH:
        return [n] + countRepeat(s, str(1 - int(z)), 0)
    elif s[0] == z:
        return countRepeat(s[1:], z, n + 1)
    else:
        return [n] + countRepeat(s[1:], str(1 - int(z)), 1)

def numToBinary(N):
    if N == 0:           
        return ''    
    elif N % 2 == 1:           
        result = numToBinary(N//2) + str(N % 2)
        return result
    else:           
        result = numToBinary(N//2) + str(N % N)
        return result

def binaryToNum(s):
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

def fillBits(N):
    neededZeros = COMPRESSED_BLOCK_SIZE - len(N)
    return ("0" * neededZeros + N)

def uncompress(S):
    runList = convertBinary(S)
    return convertRunList(runList, 0)


def convertBinary(S):
    if len(S) == 0:
        return []
    elif len(S) <= 5:
        return [binaryToNum(S)]
    else:
        return [binaryToNum(S[0:5])] + convertBinary(S[5::])

def convertRunList(S, bit):
    if len(S) == 0:
        return ''
    elif bit == 0:
        return '0' * S[0] + convertRunList(S[1:], 1)
    else:
        return '1' * S[0] + convertRunList(S[1:], 0)

def compression(S):
    originalLength = len(S)
    compressedLength = len(compress(S))
    return compressedLength / originalLength