import math

def TcToNum(binaryStr):
    return add("1", Tc(binaryStr))

def Tc(binaryStr):
    if not binaryStr:
        return ''
    elif binaryStr[0] == '0':
        return '1' + Tc(binaryStr[1:])
    else:
        return '0' + Tc(binaryStr[1:])

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

def baseBToNum(N, B):
    if len(N) <= 0:
        return 0
    else:
        return int(int(N[0]) * math.pow(B, len(N)-1)) + baseBToNum(N[1:], B)

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

print(TcToNum("10000000"))