from collections import Counter

arr1 = [7,8,3,0,5,4,2]
arr2 = [7,8,3,0,4,2]

count_arr1 = Counter(arr1)
count_arr2 = Counter(arr2)

for key in count_arr1:
    if count_arr1[key] != count_arr2[key]: print("Missing element is", key)
