# https://leetcode.com/problems/maximum-distance-in-arrays/description/

import sys

class Solution:
    # Algorithm:
    # Note: The given arrays are sorted
    # Create min1, min2 arrays which store the first two smallest values and their indices from the arrays(smallest is array[0])
    # Create max1, max2 arrays which store the first two largest values and their indices from the arrays(largest is array[-1])

    def maxDistance(self, arrays):
        max1, max2 = [-sys.maxsize, -sys.maxsize], [-sys.maxsize, -sys.maxsize]
        min1, min2 = [sys.maxsize, sys.maxsize], [sys.maxsize, sys.maxsize]

        for i, arr in enumerate(arrays):
            if arr[0] <= min1[0]:
                min2 = min1
                min1 = [arr[0], i]
            if arr[-1] >= max1[0]:
                max2 = max1
                max1 = [arr[-1], i]

        # If the min and max have different indices(means they are from diff arrays), return their abs diff
        # Else return the max value of the differences of the other min and max
        if min1[1] != max1[1]:
            return abs(min1[0] - max1[0])
        else:
            return max(abs(min1[0] - max2[0]), abs(min2[0] - max1[0]))
