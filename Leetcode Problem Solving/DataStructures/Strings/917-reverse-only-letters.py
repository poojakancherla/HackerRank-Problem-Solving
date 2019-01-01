# First add all the alphabet chars into a stack, so that when we building the reversed string we can just pop the char from stack
# Strings are immutable, so make the original string into list to modify it
# traverse through the list, if it is a alpha replace it with popped char of stack. Just adding reversed alpha characters
#  If it not alpha, then skip
# Return the list as a string
def reverse(s):
    alpha_list = []
    for char in s:
        if char.isalpha(): alpha_list.append(char)
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha(): s[i] = alpha_list.pop()

    return "".join(s)


print(reverse("a-bC-dEf-ghIj"))
