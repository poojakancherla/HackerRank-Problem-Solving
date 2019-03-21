# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

lookup = {}

def numSum(numbers):
    for num in numbers:
        if k-num in lookup.keys():
            return True
        else: lookup[num] = 1
    return False

k = int(input()) #Target sum
numbers = [int(num) for num in input().split()]
print(numSum(numbers))
