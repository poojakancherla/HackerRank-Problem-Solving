# https://www.hackerrank.com/challenges/array-left-rotation/problem


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))


    for i in (a[d:] + a[0:d]):
        print(i, end = " ")
