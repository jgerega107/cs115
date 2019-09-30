#sieve of eratosthenes to find prime numbers

def sieve(L):
    if L == []:
        return []
    else:
        return [L[0]] + sieve(filter(lambda X: X % L[0] != 0, L[1:]))

print(sieve([2,3,4,6,7,8,9]))

#the packing problem
#amount of base cases is based on amount of inputs

def subset(target, L):
    if target == 0: return True
    elif L == []: return False
    elif L[0] > target: return subset(target, L[1:])
    else:
        useIt = subset(target - L[0], L[1:])
        loseIt = subset(target, L[1:])
        return useIt or loseIt

