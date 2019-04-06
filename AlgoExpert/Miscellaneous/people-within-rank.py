# Find the number of people whose ranks are within k
# If two poeple have the same scores, then even though they have the same ranks, the next score will get the second consequtive rank
# eg: If two people have 100 scores, they both get 1st rank. The next person will get 3rd rank and not 2nd


def rank(scores, k):
    scores.sort(reverse  = True)
    count = 1; rank = 1

    curr = scores[0]
    for i in range(1, len(scores)):
        if rank > k: return count
        if scores[i] < curr:
            curr = scores[i]
            rank = count + 1        
            if rank <= k: count += 1
        else: count += 1

scores = [100, 90, 90, 90, 90, 90, 31, 12, 4]
k = 4

print(rank(scores, k))
