def coin_row(coins):
    if coins == []:
        return 0
    elif len(coins) == 1:
        return coins[0]
    else:
        evenIndexes = coins[0] + coin_row(coins[2::])
        oddIndexes = coins[1] + coin_row(coins[3::])
        return max(evenIndexes, oddIndexes)