# https://www.hackerrank.com/challenges/array-left-rotation/problem

nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

# Printing the elements of array after rotation
for i in (a[d:] + a[0:d]):
    print(i, end = " ")
