'''
Created on 9/19/19 
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Lab 3
'''


# change: takes in a total coin value and a list of possible coins. returns the smallest combination of coins to create the given value
def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        useIt = 1 + change(amount - coins[0], coins)
        loseIt = change(amount, coins[1:])
        return min(useIt, loseIt)
