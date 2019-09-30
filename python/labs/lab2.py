'''
Created on September 11th 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author Jake Gerega
username: jgerega
'''


def dot(L, K):
    if L == [] or K == []:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

#computes dot product of two lists. takes in two lists and outputs an integer

def explode(S):
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])

#separates characters in a string into an array. takes in one string and outputs a list

def ind(e, L):
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

#computes index of first instance of e in a list. takes in a value and a list and returns an integer representing index of e in L

def removeAll(e, L):
    if L == []:
        return L
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

#removes all instances of e in L list. takes in a value e and a list L

def deepReverse(L):
    if L == []:
        return L
    elif type(L[0]) == type([]):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]

#takes a list and reverses it. also works with nested lists. 

def myFilter(f, L):
    if L == []:
        return L
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:]) 
    
#rewrite of filter function using recursion, takes in a function and a list, outputs a list




