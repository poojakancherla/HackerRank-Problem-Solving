def rotate(nums, k):
    k = k % len(nums)
    nums = nums[(len(nums) - k) : len(nums)] + nums[0 : (len(nums) - k)]

    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))