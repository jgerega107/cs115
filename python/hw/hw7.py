import math

def TcToNum(binaryStr):
    isNeg = isBinNeg(binaryStr)
    tc = add(TcToNumHelper(binaryStr), '1')
    if isNeg:
        return baseBToNum(tc, 2) * -1
    else:
        return baseBToNum(binaryStr, 2)

def TcToNumHelper(binaryStr):
    if not binaryStr:
        return ''
    else:
        if binaryStr[0] == '1':
            return '0' + TcToNumHelper(binaryStr[1:])
        else:
            return '1' + TcToNumHelper(binaryStr[1:])

def isBinNeg(binaryStr):
    if binaryStr[0] == '1':
        return True
    return False

def baseBToNum(N, B):
    if len(N) == 0:
        return 0
    else:
        return int(int(N[0]) * math.pow(B, len(N)-1)) + baseBToNum(N[1:], B)

def add(N1, N2):
    n1dec = baseBToNum(N1, 2)
    n2dec = baseBToNum(N2, 2)
    sum = n1dec + n2dec
    return numToBaseB(sum, 2)

def numToBaseB(N, B):
    if N <= 0:
        return ''
    else:
        return numToBaseB(N // B, B) + str(N % B)

def fillBits(N):
    if len(N) < 8:
        neededZeros = 8 - len(N)
        return "0" * neededZeros + N
    return N

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