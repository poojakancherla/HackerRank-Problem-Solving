def reverseWord(i, j, array):
    while i < j:
        array[i], array[j] = array[j], array[i]    
        i += 1; j -= 1

def reverseString(array):    
    reverseWord(0, len(array)-1, array)
    i = j = 0
    while j < len(array):
        if array[j] == ' ': 
            reverseWord(i, j-1, array) 
            while array[j] == ' ': j += 1
            i = j
        j += 1
    if i < j: reverseWord(i, j-1, array)

    return array

array = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',' ',' ',' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
array = ["1", "2", "3", " ", "4", "5", "6", " ", "7", "8", "9"]
print(reverseString(array))