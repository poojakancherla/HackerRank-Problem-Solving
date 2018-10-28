# https://www.hackerrank.com/challenges/arrays-ds/problem

def reverseArray(a):
    rev = []
    for i in range(len(a) - 1, -1, -1):
        rev.append(a[i])
    return rev

print(reverseArray([1,2,3,4]))
