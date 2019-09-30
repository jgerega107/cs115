#the knapsack problem
#you have a weigth with a value associated with it
#find the combination with the most value while staying <= the capacity of the knapsack

def knapsack(c, L):
    if c == 0 or L ==[]:
        return 0
    elif L[0][0] > c:
        return knapsack(c, L[1:])
    else:
        useIt = L[0][1] + knapsack(target-L[0][0], L[1:])
        loseIt = knapsack(target, L[1:])
        return max(useIt, loseIt)

#LCS DNA Alignment

def LCS(s1, s2):
    if s1 == "" or s2 == "": return 0
    else:
        if s1[0] == s2[0]:
            return 1 + LCS(s1[1:], s2[1:])
        else:
            first = LCS(s1, s2[1:])
            last = LCS(s1[1:], s2)
            return max(first, last)