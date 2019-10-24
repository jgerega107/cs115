"""
Created on 10/22/19
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
"""
import math

FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

#numToBaseB: takes in a base 10 number N and a base B and returns N in base B
def numToBaseB(N, B):
    if N <= 0:
        return ''
    else:
        return numToBaseB(N // B, B) + str(N % B)

#baseBToNum: takes in a base B number and a base B and returns a number in base 10
def baseBToNum(N, B):
    if len(N) <= 0:
        return 0
    else:
        return int(int(N[0]) * math.pow(B, len(N)-1)) + baseBToNum(N[1:], B)

#baseToBase: takes in a number of base B1 and returns a number of base B2
def baseToBase(B1, B2, SinB1):
    decimal = baseBToNum(SinB1, B1)
    return numToBaseB(decimal, B2)

#add: takes in two base 2 numbers and returns the result of adding them together while still keeping base
def add(N1, N2):
    n1dec = baseBToNum(N1, 2)
    n2dec = baseBToNum(N2, 2)
    sum = n1dec + n2dec
    return numToBaseB(sum, 2)

#addB: takes in two base 2 numbers and returns the result of adding them together while still keeping base (without converting to decimal mid process)
def addB(N1, N2):
    if not N1 and not N2:
        return "0"
    else:
        return addWithCarry(N1, N2, "0")

#addWithCarry: helper function for addB, allows extra carryIn parameter to mimic a full adder circuit
def addWithCarry(N1, N2, carryIn):
    if N1 == "0" and not N2:
        return carryIn
    elif not N1 and N2 == "0":
        return carryIn
    elif not N1 and not N2 and carryIn == 1:
        return carryIn
    elif not N1 and not N2:
        return ""
    elif not N2 and N1:
        sumBit, carryBit = FullAdder[(N1[-1], "0", carryIn)]
        return addWithCarry(N1[:-1], "0", carryIn) + sumBit
    elif not N1 and N2:
        sumBit, carryBit = FullAdder[("0", N2[-1], carryIn)]
        return addWithCarry("0", N2[:-1], carryIn) + sumBit
    else:
        sumBit, carryBit = FullAdder[(N1[-1], N2[-1], carryIn)]
        return addWithCarry(N1[:-1], N2[:-1], carryBit) + sumBit

print(addB("11", "1"))