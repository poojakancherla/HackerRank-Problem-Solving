def twoSum(numbers, target):
    i, j = 0, len(numbers)-1
    while j >= 0 and i < len(numbers):
        if numbers[i] + numbers[j] == target: return sorted([i+1,j+1])
        if numbers[i] + numbers[j] < target: i += 1
        else: j -= 1
        

numbers = [2,7,11,15] 
target = 9
print(twoSum(numbers, target))