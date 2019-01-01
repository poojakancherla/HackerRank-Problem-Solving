def firstUniqChar(self, s):
        # Make a counter for the string. Traverse through the counter and return its index in the string when the value is 1.
        counter = Counter(s)
        for c in counter:
            if counter[c] == 1:
                return s.index(c)
        return -1

print(firstUniqChar("leetcode"))
