# O(N) time complexity and O(N) space complexity

# def twoNumberSum(array, targetSum):
	# if len(array) == 0: return []
	# lookup = {}
	# for num in array:
	# 	if targetSum - num in lookup: return sorted([num, targetSum - num])
	# 	else:
	# 		lookup[num] = 1
	# return []

#############################################################################################################

# O(NlogN) time complexity and O(1) space complexity

def twoNumberSum(array, targetSum):
    if len(array) == 0: return []
    array = sorted(array)

    leftPointer = 0
    rightPointer = len(array) - 1

    while(leftPointer < rightPointer):

        curr_sum = array[rightPointer] + array[leftPointer]

        if curr_sum is targetSum: return [array[leftPointer], array[rightPointer]]
        elif curr_sum < targetSum: leftPointer += 1
        elif curr_sum > targetSum: rightPointer -= 1

    return []

print(twoNumberSum([4,6,1], 5))
