def knapsackVal(capacity, L):
    '''Given a capacity and a list of pairs [w,v]
    where w and v are weight and value of an object
    find the maximum value that can be obtained by choosing objects
    without the total weight exceeding the capacity
    '''
    if capacity == 0 or L == []:
        return 0
    elif L[0][0] > capacity:
        return knapsackVal(capacity, L[1:])
    else:
        useIt = L[0][1] + knapsackVal(capacity - L[0][0], L[1:])
        loseIt = knapsackVal(capacity, L[1:])
        return max(useIt, loseIt)

print(knapsackVal(30, ))

#for tests, study LCS and useItOrLoseIt
