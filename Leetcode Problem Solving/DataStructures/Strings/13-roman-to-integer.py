# For the vhars in the string, if curr element is less than the next element then it should be subtracted from the result
# Or else it should be added to the result
# Since the loop doesn't run for the last char, we need to separately add it to the result
def romanToInt(s):
    romanLookup = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(s) -1):
        if romanLookup[s[i]] < romanLookup[s[i+1]]: result -= romanLookup[s[i]]
        else: result += romanLookup[s[i]]
    return result + romanLookup[s[-1]]

print(romanToInt("MCMXCIV"))
