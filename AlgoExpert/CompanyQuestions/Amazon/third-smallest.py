import sys
def thirdSmall(nums):
    if len(nums) < 3: return 0  
    first, second, third = sys.maxsize, sys.maxsize, sys.maxsize
    for num in nums:
        if num < first:
            third = second; second = first; first = num
        elif num < second:
            third = second; second = num
        elif num < third:
            third = num
    return first,second,third

nums = (5,8,4,0,3,7)
print(thirdSmall(nums))
