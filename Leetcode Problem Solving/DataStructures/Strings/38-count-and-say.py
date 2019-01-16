############################################################################################################################
def countAndSay1(n):
    term = '1'
    for _ in range(n - 1):
        # To form count and say from the current term
        seq_arr = [[term[0], 1]]

        for i in range(1, len(term)):
            if term[i] == term[i-1]: seq_arr[-1][1] += 1
            else: seq_arr.append([term[i], 1])
        # To form the next term
        term = ''
        for ele in seq_arr:
            term += (str(ele[1]) + str(ele[0]))

    return term
##############################################################################################################################

def countAndSay2(n):
# For example, if the term is 21, the next element would be "one 2 and one 1" which will written as 1211
# We count the seq of same numbers then we say it and the number, we do this for all the elements in the term
# For example 1121, "two 1s one 2 and one 1" which will be 211211
# To create this, we have to add both the number and its count in the array
# Add the first number and the count will be 0 now. Go to the next element, if it is same then increase the counter
# Else, it means there's a different element so add it and its counter as 1 to the arr and do this for the whole term
# When we get the final array, for each number and its count in the array, append all the counts and numbers as strings into result string
# This is the current string
    def calc(term):
        arr = [[term[0], 1]]
        res = ""
        for i in range(1, len(term)):
            if term[i] == term[i - 1]: arr[-1][1] += 1
            else: arr.append([term[i], 1])
        for val in arr:
            element, count = val
            res += str(count) + str(element)
        return res
# We start here
# Since n >= 1 we take the first element as 'prev' and start forming the sequences from n = 2
# We form the curr seq by counting and saying the prev seq, using the calc method
# And we do this n-1 times and not n times since we already declared the seq for n = 1
# And for every iteration, after calculating curr, prev becomes curr in order to calculate the next curr
    prev = "1"
    for i in range(n - 1):
        cur = calc(prev)
        prev = cur

    return cur
###################################################################################################################################

print(countAndSay1(5))
