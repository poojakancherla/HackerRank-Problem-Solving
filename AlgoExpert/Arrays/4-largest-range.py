# Used dictionary to make the lookup of a consequtive number in constant time
# For every num in array to need to check its left and right consequtive numbers and calculate its range size
# If it is bigger that the longest range which is initially zero, we update the longest range and also store the end elements
# If it is not bigger than the longest range we found so far, it doesn't update the longest range
# First we need to put all the nums into the dictionary
# When we visit each number the current lenth becomes 1
# For every number, we see if it has a left(which is num-1) and a right(which is num+1) consequtive numbers
# If there is a left we check if that a left and we keep going until there is no more. And for every left the currLenth increases
# Do the same for right number
# Now we have currLength which is the range of both left and right numbers together
# If this is > longestLength then update the longest length and the end elements
# Now if we go to the next num in array and if it is already part of one of the ranges we don't need to check its range as its going to be the same
# So in order to avoid duplicate calculations, we should mark which nums have been visited already and should not check for them
# To do that, start by creating the dictionary and asiigning true to all of them, which means they haven't been checked
# And while traversing the nums, mark their values in the dict to false to say that they are already part of a range and need not be checked agn

def largestRange(array):
    nums = {}
    longestLength = 0
    bestRange = []

    for num in array: nums[num] = True

    for num in array:
        if not nums[num]: continue # If the num has been marked false, skip it
        nums[num] = False
        currLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currLength += 1
            right += 1
        if currLength > longestLength:
            longestLength = currLength
            bestRange = [left + 1, right - 1]

    return bestRange

print(largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))
print(largestRange([1,2]))
print(largestRange([4,2,1,3,6]))
