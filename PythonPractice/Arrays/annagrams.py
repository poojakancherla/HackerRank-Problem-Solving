import collections

def isAnagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2): return False
    
    count = collections.Counter(s1)

    for char in s2:
        if count[char]: count[char] -= 1

    for key in count:
        if count[key]: return False

    return True
    

s1 = "boon noob"
s2 = "noob no bo"
print(isAnagram(s1, s2))
    