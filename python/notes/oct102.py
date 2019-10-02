#memoization: recursive functions tend to make many recursive calls with the same set of parameters- redundant computation
#memoization is a fast cache or look up table to get a result of an already computed recursive call
#alternative is to use loops or iterations but many problems can be solved elegantly using recursion
#memoization is the answer for efficiency


#standard fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#memoization fibonacci
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    else:
        print("Computing fibonacci({})...".format(n))
        if n == 0 or n == 1:
            return 1
        else:
            result = fibonacci_memo(n)
        memo[n] = result
        return result