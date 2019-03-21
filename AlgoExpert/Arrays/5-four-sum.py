# Problem: Given a non-empty list of distinct integers and an integer representing the target sum, find all quadruplets in the list that sum up
# to the target sum and return a 2D array of all these qudruplets in no particular order. If none, return empty array


### Algorithm ###

# O(N^3) time complexity and O(N) space complexity

# First sort the array
# Solve this problem by extending the three number sum problem
# Loop through the numbers and find the three number sum
# The loop for three number runs from the next element of the loop of the four number sum
# If the three num sum plus the fourth element = target sum, then add all the numbers as a list to result
# Else if the three num sum plus the fourth element < target sum, then increment the left pointer (To move closer to the target sum)
# Else, this means that the three num sum plus the fourth element > target sum. Then decrement the right counter


def fourNumberSum(array, targetSum):
    array.sort()

    result = []
    for k in range(len(array) - 3):
        for i in range(k+1, len(array) - 2):
            left = i + 1
            right = len(array) - 1

            while left < right:
                threeNumSum = array[i] + array[left] + array[right]
                if threeNumSum + array[k] == targetSum:
                    result.append(sorted([array[k], array[i] , array[left] , array[right]]))
                    left += 1; right -= 1
                elif threeNumSum + array[k] < targetSum: left += 1;
                else: right -= 1
    return result

print(fourNumberSum([7,6,4,-1,1,2], 16))
