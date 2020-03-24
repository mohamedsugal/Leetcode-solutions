def coinChange(coins, amount):
    change = [amount+1] * (amount+1)
    change[0] = 0
    for i in range(len(change)):
        for coin in coins:
            if coin <= i:
                change[i] = min(change[i], change[i-coin]+1)

    if change[amount] > amount:
        return -1
    return change[amount]


coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

