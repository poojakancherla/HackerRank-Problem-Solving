#  O(N^2) time and O(N) space

# First, sort the array in ascending order
# For every element at 'i' in the array, take left pointer at 'i+1' and right pointer at len(array) - 1. Then move left and right pointers, becaause if we move only one
# If the sum of elements at all these pointers is equal to target, then add these elements as a list to the result
# If this sum < target, then increment the left pointer. Since the array is sorted, moving the left pointer to the right increases the sum
# If the sum > target then decrement the right pointer so that the sum decreases
# We can perform these operations only while left < right

def threeNumberSum(array, targetSum):
    array.sort()

    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                triplets.append([array[i] , array[left] , array[right]])
                left += 1; right -= 1
            elif currSum < targetSum: left += 1
            else: right -= 1

    return triplets



print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0))
