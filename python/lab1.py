#Jacob Gerega
#I pledge my honor that I have abided by the Stevens Honor System.

from python.cs115 import map
import math

def inverse(x):
    return 1.0/x

def add(x,y):
    return x+y
    
def e(n):
    list1 = [1]
    list2 = list(range(1, n+1))
    list2 = map(math.factorial, list2)
    list2 = map(inverse, list2)
    return sum(list1+list2)

def error(n):
    sum = e(n)
    return abs(math.e - sum)
