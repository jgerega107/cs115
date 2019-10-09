'''
Created on 10/4/19
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.
wn = turtle.Screen()
turtle = turtle.Turtle()
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

def snowflake(trunk_length, levels):
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    snowflakeSide(trunk_length, levels)
    turtle.right(120)
    pass  # TODO

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
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
