def maxCoins(piles):
    piles.sort()
    n = len(piles)
    numberOfCoins = n // 3
    coins = 0
    count = 0
    i = n - 2
    while count < numberOfCoins and i >= 1:
        coins += piles[i]
        count += 1
        i -= 2
    return coins


