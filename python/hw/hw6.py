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

def baseToBase(B1, B2, SinB1):
    decimal = baseBToNum(SinB1, B1)
    return numToBaseB(decimal, B2)

def add(N1, N2):
    n1dec = baseBToNum(N1, 2)
    n2dec = baseBToNum(N2, 2)
    sum = n1dec + n2dec
    return numToBaseB(sum, 2)

#addB
