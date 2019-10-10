'''
Created on 10/8/19
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 4
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.
wn = turtle.Screen()
turtle = turtle.Turtle()

#snowflakeSide: takes in a trunk length as integer, takes in levels as integer, makes turtle create one side of said length and level
def snowflakeSide(trunk_length, levels):
    if levels == 0:
        turtle.forward(trunk_length)
    else:
        snowflakeSide(trunk_length, levels - 1)
        turtle.left(60)
        snowflakeSide(trunk_length, levels - 1)
        turtle.right(120)
        snowflakeSide(trunk_length, levels - 1)
        turtle.left(60)
        snowflakeSide(trunk_length, levels - 1)

#snowflake: uses previous snowflakeSide with same parameters but puts together sides to create a full snowflake
def snowflake(trunk_length, levels):
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    pass  # TODO

#fast_change: takes in an amount and a list of possible coins and returns the minimum number of coins required to get given amount but uses memoization for speed
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount == 0:
            return 0
        elif coins == ():
            return float("inf")
        elif coins[0] > amount:
            return fast_change_helper(amount, coins[1:], memo)
        else:
            useIt = 1 + fast_change_helper(amount - coins[0], coins, memo)
            loseIt = fast_change_helper(amount, coins[1:], memo)
            memo[(amount, coins)] = min(useIt, loseIt)
            return min(useIt, loseIt)
        pass  # Write your code here

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a snow flake
snowflake(800, 3)
