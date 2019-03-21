# Find all two element pairs from two arrays which sum to a given number X

# Input:
A = [1, 2, 4, 4, 6, 7, 7, 8]
B = [1, 2, 3, 4, 4, 8]
X = 13

# Algorithm:
# Sort the arrays in ascending order
# Take an initial min_diff btwn the target sum and the sum of the elements frm the arrays as "inf"
#  Take two pointers: i at first index of array 1 and j at last index of array 2
# i moves to the end of array 1 and j moves to the start of array 2
# If the current diff < min_diff then update min_diff and check if ou found the result

from sys import maxsize as inf
from heapq import heappop as pop, heappush as push
from collections import defaultdict, deque

def getAllPairsWithSum(summ, A, B):
    lookupA = defaultdict(deque)
    result = []

    for i in range(len(A)): lookupA[A[i]].append(i)
    print(lookupA)
    for i in range(len(B)): # O(n)
        complement = summ - B[i]
        while(complement in lookupA and len(lookupA[complement])):
            result.append([lookupA[complement].popleft(), i])
    return result

def closestSumPairToX(A, B, X):
    A.sort(); B.sort()
    min_diff = inf
    i = 0; j = len(B) - 1
    result = []; ans = None

    while i < len(A) and j >= 0:
        summ = (A[i] + B[j])
        curr_diff = abs(X - summ)
        if curr_diff <= min_diff:
            print(summ, curr_diff, "|", i, j, "|", A[i], B[j])
            min_diff = curr_diff
            if summ <= X: push(result,((-summ, [i, j])))
        if summ < X: i += 1
        else: j -= 1

    finalResult = getAllPairsWithSum(-pop(result)[0], A, B)
    return finalResult



print(closestSumPairToX(A, B, X))
