# Brute-force method with O(n^3) time and O(1) space
def longestPalindromic_brute(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]

            if len(substring) > len(longest) and substring == substring[::-1]:
                longest = substring

    return longest



# Better method with O(n^2) time and O(1) space

# We need to check two types of combinations: even length and odd length
# In odd length, we expand to the left and right of the element at a particular index and everytime check if its a palindrome
# Then we get the max of the odd and even length palindromes for that iteration and update the current longest
# Then we compare the current longest with longest and update likewise
# For all these comparisions we only store the indices and then calculate the max based on these

def longestPalindromic(string):
    longest = [0,1]
    for i in range(1, len(string)):
        even = getLongesetPalindromeFrom(string, i-1, i)
        odd = getLongesetPalindromeFrom(string, i-1, i+1)        
        currLongest = max(even, odd, key = lambda x: x[1] - x[0])
        longest = max(longest, currLongest, key = lambda x: x[1] - x[0])

    return string[longest[0] : longest[1]]

def getLongesetPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1

    return [leftIdx+1, rightIdx]
    

print(longestPalindromic("abaxyzzyxf"))
