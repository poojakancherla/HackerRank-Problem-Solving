from collections import Counter
def missing(arr1, arr2):
    counter = Counter(arr2)
    for num in arr1:
        if not counter[num]: return num
            
arr1 = [4, 8, 12, 9, 3]
arr2 = [4, 8, 9, 3]
print(missing(arr1, arr2))