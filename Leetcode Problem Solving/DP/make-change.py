import sys

def minCoins(n, coins):
    def change(n, coins):
        if n == 0: return 0
        minCoins = sys.maxsize

        for coin in coins:
            if n-coin >= 0:
                currMin = change(n-coin, coins)
                minCoins = min(minCoins, currMin)
        return minCoins + 1

    return change(n, coins)  

print(minCoins(12, [10, 6, 1]))