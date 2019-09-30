#dictionaries
"""
D = {} #create a dictionary
D[k] = v #make key k with value v OR replace old value if k already in D
D[k] #get value under key k
k in D #whether k is a key in D
D.keys() #get sequence of all keys in D
D.values() #get sequence of all values in D
D.items() #get sequence of all key value pairs in D

v can be any value
k must be an immutable type(string, int, tuple of immutables)

EXAMPLES
given a list, get frequency count of occurrences of items in the list. keep the key value pair in the dictionary: item, # of occurrences.
"""

#L = [1,3,3,1,2,5]
#as a dictionary [(1,2),(2,1),(3,2),(5,1)] FIRST VALUE IS ITEM, SECOND NUMBER IS AMOUNT OF OCCURRENCES
def updateFreqCnt(dict):
    def update(x):
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
        return update

def freqCounts(L):
    freqDict = {}
    map(updateFreqCnt(freqDict), L)
    return list(freqDict.items())

print(freqCounts([3,2,3,11,2,5,2]))

