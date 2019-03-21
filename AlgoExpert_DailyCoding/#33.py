# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def print_median(seq):
    for i in range(len(seq)):
        currList = seq[:i+1]
        print(calc_median(currList))

def calc_median(l):
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

seq = [2,1,5,7,2,0,5]
print_median(seq)