"""
Created on 9/23/19
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - HW 3
"""


# change: takes in a total coin value and a list of possible coins. returns the smallest combination of coins to create the given value
def giveChange(amount, coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        useIt = 1 + giveChange(amount - coins[0], coins)
        loseIt = giveChange(amount, coins[1:])
        return min(useIt, loseIt)