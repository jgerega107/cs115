import math
"""
Jacob Gerega
10/31/19
I pledge my honor that I have abided by the Stevens Honor System.
"""

#takes in a binary string and returns the twos complement in base 10
def TcToNum(binaryStr):
    isNeg = isBinNeg(binaryStr)
    tc = add(TcToNumHelper(binaryStr), '1')
    if isNeg:
        return baseBToNum(tc, 2) * -1
    else:
        return baseBToNum(binaryStr, 2)

#helper method for TcToNum, actually does the flipping, returns a binary string
def TcToNumHelper(binaryStr):
    if not binaryStr:
        return ''
    else:
        if binaryStr[0] == '1':
            return '0' + TcToNumHelper(binaryStr[1:])
        else:
            return '1' + TcToNumHelper(binaryStr[1:])

#helper method for TcToNum, checks if string is negative, returns boolean
def isBinNeg(binaryStr):
    if binaryStr[0] == '1':
        return True
    return False

#converts any base number to decimal (in this case, binary), returns a number in base 10
def baseBToNum(N, B):
    if len(N) == 0:
        return 0
    else:
        return int(int(N[0]) * math.pow(B, len(N)-1)) + baseBToNum(N[1:], B)

#adds any given two binary numbers together, returns a binary string
def add(N1, N2):
    n1dec = baseBToNum(N1, 2)
    n2dec = baseBToNum(N2, 2)
    sum = n1dec + n2dec
    return numToBaseB(sum, 2)

#converts a number in to base B (in this case, binary), returns a string in base 2
def numToBaseB(N, B):
    if N <= 0:
        return ''
    else:
        return numToBaseB(N // B, B) + str(N % B)

#fills in the rest of a given binary string with zeros
def fillBits(N):
    if len(N) < 8:
        neededZeros = 8 - len(N)
        return "0" * neededZeros + N
    return N

#takes in a number and converts it to a twos complement binary string. returns binary string
def NumToTc(num):
    if num < -128 or num > 127:
        return 'Error'
    elif num < 0:
        binaryStr = fillBits(numToBaseB(num*-1, 2))
        tc = TcToNumHelper(binaryStr)
        tcp2 = add(tc, '1')
        return tcp2
    else:
        binaryStr = fillBits(numToBaseB(num, 2))
        return binaryStr