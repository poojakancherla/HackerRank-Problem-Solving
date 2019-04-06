# Below is the algorithm to find if a given decimal is a palindrome or not
# This algorithm doesn't convert the number to string in order to find if its a palindrome, hence takes constant space
# Negative numbers cannot be palindrome
# We loop through the number and compare the most significant and least significant bits(first and last bits)
# The length of a number can be found by floor of log10(x) + 1
# To get the most significant bit, first get the mask -> 10 ** (numBits - 1). Then divide the number with the mask
# If they are equal, update the number to compare the next bits by removing the LSB and MSB
# Also update the mask
# Takes O(n) time and O(1) space

import math
def palindrome(x):
    if x <= 0: return x == 0
    numBits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (numBits - 1)

    for _ in range(numBits // 2):
        if x // msd_mask != x % 10: return False
        x %= msd_mask # Removing the MSB
        x //= 10 # Removing the LSB
        msd_mask //= 100
    return True

print(palindrome(-13231))
