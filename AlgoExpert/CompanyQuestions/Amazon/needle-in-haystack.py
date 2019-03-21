def grep1(haystack, needle):
    result = []
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle: result.append(i)
    return result


def grep2(haystack, needle):
    result = []
    i = j = 0
    while i <= j and i < len(haystack) - len(needle) + 1 and j < len(haystack):
        if haystack[i:j+1] == needle:
            result.append(i)
            j += 1
            i = j
        else:
            if haystack[j] == needle[j]:
                j += 1
            else:
                i += 1
                j += 1







haystack = "helloollll"
needle = "ll"
print(grep2(haystack, needle))
