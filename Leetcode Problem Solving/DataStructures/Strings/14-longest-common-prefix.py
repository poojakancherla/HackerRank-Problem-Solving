# https://leetcode.com/problems/longest-common-prefix/description/

arr = ["flower","flow","flight"]
minLength = min(map(len, arr))

for i in range(minLength):
    for j in range(len(arr) - 1):
        if arr[j] == arr[j+1]: prefix += arr[i]
