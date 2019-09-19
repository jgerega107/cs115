'''
Created on September 10th 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author Jake Gerega
username: jgerega
'''

from python.cs115 import map, reduce

def mult(x,y):
    return x*y

def add(x,y):
    return x+y

def factorial(n):
    list1 = list(range(1, n+1))
    return reduce(mult, list1)

def mean(L):
    sum = reduce(add, L)
    return sum / len(L)

def divides(n):
    def div(k):
        return n % k == 0
    return div

def primes(n):
    list1 = map(divides(n), list(range(2,n)))
    return not True in list1


    

