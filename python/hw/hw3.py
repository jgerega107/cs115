"""
Created on 9/23/19
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - HW 3
"""


# giveChange: takes in a total coin value and a list of possible coins. returns the smallest combination of coins to create the given value as well as a sublist of all used coins
def giveChange(amount, coins):
    if amount == 0:
        return [0, []]
    elif coins == []:
        return [float("inf"), []]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        useItList = giveChange(amount - coins[0], coins)
        loseItList = giveChange(amount, coins[1:])
        minimum = min(useItList[0] + 1, loseItList[0])
        if minimum == useItList[0] + 1:
            return [minimum, useItList[1] + [coins[0]]]
        else:
            return [minimum, loseItList[1]]