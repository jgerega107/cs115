"""
Created on 9/26/19
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Lab 4
"""

#coin_row: takes in a list of coins and returns the highest possible combination without using adjacent coins
def coin_row(coins):
    if coins == []:
        return 0
    elif len(coins) == 1:
        return coins[0]
    else:
        evenIndexes = coins[0] + coin_row(coins[2::])
        oddIndexes = coin_row(coins[1::])
        return max(evenIndexes, oddIndexes)

#coin_row_with_values: takes in a list of coins and returns the highest possible combination without using adjacent coins and the coins used

def coin_row_with_values(coins):
    if coins == []:
        return [0, []]
    else:
        evenIndexes = coin_row_with_values(coins[2::])
        oddIndexes = coin_row_with_values(coins[1::])
        maximum = max(evenIndexes[0] + coins[0], oddIndexes[0])
        if maximum == evenIndexes[0] + coins[0]:
            return [maximum, [coins[0]] + evenIndexes[1]]
        else:
            return [maximum, oddIndexes[1]]