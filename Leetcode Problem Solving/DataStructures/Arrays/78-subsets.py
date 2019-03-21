def subsets(nums):
    arr1 = []
    arr2 = []
    for i in range(len(nums)):
        arr1.insert(0, [nums[i]])
        arr2.append(nums[:i] + nums[i+1:])
    return [[]] + arr1 + arr2 + [nums]

print(subsets([1,2,3]))