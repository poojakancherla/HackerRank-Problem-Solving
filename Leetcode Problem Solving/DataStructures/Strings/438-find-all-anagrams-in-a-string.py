# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import deque
from collections import Counter

def findAllNeedles(hayStack, needle):
    def delFromCounter(i):
        dq[hayStack[i]] -= 1
        if dq[hayStack[i]] == 0: del dq[hayStack[i]]

    def addToCounter(i):
        dq[hayStack[i]] += 1

    dq = Counter(hayStack[: len(needle)])
    needle = Counter(needle); res = []

    for i in range(len(hayStack) - (len(needle) - 1)):
        if dq == needle: res.append(i)
        if i + len(needle) < len(hayStack):
            delFromCounter(i)
            addToCounter(i + len(needle))
    return res

print(findAllNeedles("adsksjdfjsadaisfasd", "asd"))

def findAllNeedles(hayStack, needle):
    dq = deque(hayStack[: len(needle)])
    needle = deque(needle); res = []

    for i in range(len(hayStack) - (len(needle) - 1)):
        if dq == needle: res.append(i)
        if i + len(needle) < len(hayStack):
            dq.popleft()
            dq.append(hayStack[i + len(needle)])
    return res

print(findAllNeedles("asdksjdfjasdaisfasd", "asd"))

























#

from collections import Counter
def findAnagrams(s, p):
    pCounter = Counter(p); sCounter = Counter(s[:len(p)-1])
    result = []

    for i in range(len(p)-1, len(s)):
        sCounter[s[i]] += 1
        if sCounter == pCounter: result.append(i-len(p)+1)
        sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
        if sCounter[s[i-len(p)+1]] == 0: del sCounter[s[i-len(p)+1]]

    return result
print(findAnagrams("adsksjdfjsadaisfasd", "asd"))
