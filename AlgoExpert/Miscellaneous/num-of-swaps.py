arr = [7,1,3,2,4,5,6]

def swap(x, y, arr):
    arr[x], arr[y] = arr[y], arr[x]    

def min_swaps(arr):
    arr = [(ele, index) for index,ele in enumerate(arr)]
    arr.sort(); count = 0; i = 0

    while(i < len(arr)):
        if i == arr[i][1]: 
            i += 1
            continue
        else:
            swap(arr[i][1], i, arr)
            count += 1
        
        if i != arr[i][1]:
            i -= 1 # If the element at index i is not the right element, then swap again until it is right
        
        i += 1

    return count
        

print(min_swaps(arr))