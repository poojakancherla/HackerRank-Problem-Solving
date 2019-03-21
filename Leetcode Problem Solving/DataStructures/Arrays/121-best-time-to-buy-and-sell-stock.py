import sys

def maxProfit(prices):
    min = sys.maxsize
    maxProfit = 0

    for i in range(len(prices)):
        if prices[i] < min: 
            min = prices[i]
        else: 
            if prices[i] - min > maxProfit:
                maxProfit = prices[i] - min
    
    return maxProfit

prices = [7,6,4,3,1]
print(maxProfit(prices))