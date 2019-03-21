def minCost(cost):
    for i in range(2, len(cost)):
        cost[i] = min(cost[i-2], cost[i-1]) + cost[i]

    return min(cost[-1], cost[-2])

print(minCost([1,3,1]))