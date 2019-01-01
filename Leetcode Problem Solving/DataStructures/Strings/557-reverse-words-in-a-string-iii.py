def reverseWords(s):

    return " ".join(word[::-1] for word in s.split())

print(reverseWords("Let's take LeetCode contest"))
