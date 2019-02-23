def isPalindrome(s):
    for i in s:
        if not i.isalnum():
            s = s.replace(i, '')

    if s.lower() == s[::-1].lower(): return True
    return False
print(isPalindrome(""))
