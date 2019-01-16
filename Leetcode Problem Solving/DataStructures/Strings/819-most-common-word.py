# https://leetcode.com/problems/most-common-word/description/

# 1. First replace all the punctuations with space so that we are only left with words with spaces between, doesn't matter if there is
#    double space between words
# 2. NOw convert the string into lower case since the problem is not case sensitive and split it
# 3. We are left with a list of words in lowercase and without any punctuation marks
# 4. Now just find the word that is not in the banned list of words and occurs the most(using dictionary)

def mostCommon(paragraph, banned):
    d = {}
    punctuation = ['!', '?', ',', ';', '.', '\'']

    for ch in punctuation:
        if ch in paragraph: paragraph = paragraph.replace(ch, ' ')

    paragraph = paragraph.lower().split()

    for word in paragraph:
        if not word in (bannedWord for bannedWord in banned):
            if word in d: d[word] += 1
            else: d[word] = 1

    maxi = ('', 0)
    for key, val in d.items():
        if d[key] > maxi[1]:
            maxi = (key, d[key])

    return maxi[0]



print(mostCommon("a, a, a, a, b,b,b,c, c", ["a"]))
