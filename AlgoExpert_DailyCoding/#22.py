# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].


def sentenceFormation(dict, string):
    i = 0; j = 1; result = []
    foundTillIndex = -1

    while i <= j and i < len(string) and j < len(string):
        word = string[i : j+1]
        if word not in dict or dict[word] == 0: j += 1
        else:
            result.append(word)
            dict[word] = 0 # To represent that we have already used this key
            foundTillIndex = j
            j = j + 1
            i = j

    if foundTillIndex < len(string) - 1: return []
    return result


dict = {'apple': 1, 'pen': 1}
string = "applepenapple"

# dict = {'aaaa': 1, 'aaa' : 1}
# string = "aaaaaa"

print(sentenceFormation(dict, string))
