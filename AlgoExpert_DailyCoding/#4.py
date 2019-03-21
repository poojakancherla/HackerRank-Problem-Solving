# Maximum subarray problem

# Algorithm: Kadane's Algorithm

arr = [-6,-5,-4,-3,-2,-1]

currSum = maxSum = arr[0]

for num in arr[1:]:
    currSum = max(currSum + num, num)
    maxSum = max(maxSum, currSum)

print(maxSum)
