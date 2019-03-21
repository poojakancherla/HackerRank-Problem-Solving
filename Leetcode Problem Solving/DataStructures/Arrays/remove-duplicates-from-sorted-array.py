def remove(nums):
    if not len(nums): return 0
    length = 0
    for i in range(len(nums)-1):
        if nums[i+1] != nums[i]:
            length += 1
            nums[length] = nums[i+1]
            
    return length + 1
print(remove([1,1,2]))