def coin_row(coins):
    if coins == []:
        return 0
    elif len(coins) == 1:
        return coins[0]
    else:
        evenIndexes = coins[0] + coin_row(coins[2::])
        oddIndexes = coin_row(coins[1::])
        return max(evenIndexes, oddIndexes)

def coin_row_with_values(coins):
    if coins == []:
        return [0, []]
    else:
        evenIndexes = coin_row_with_values(coins[2::])
        oddIndexes = coin_row_with_values(coins[1::])
        maximum = max(evenIndexes[0], oddIndexes[0])
        if maximum == evenIndexes[0]:
            return [evenIndexes[0], [coins[0]] + evenIndexes[1]]
        else:
            return [oddIndexes[0], [coins[0]] + oddIndexes[1]]