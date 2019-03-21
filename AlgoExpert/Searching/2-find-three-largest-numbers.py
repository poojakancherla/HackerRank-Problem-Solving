import sys
def largestThree(array):
    first = -sys.maxsize
    second = first
    third = first
    for num in array:
        if num > first:
            if second >= third: third = second            
            if first >= second: second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third: 
            third = num
    return [third, second, first]
print(largestThree([10,5,9,10,12]))