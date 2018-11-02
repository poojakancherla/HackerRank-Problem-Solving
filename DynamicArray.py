#  https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamicArray(n, queries):
    seqList=[[] for x in range(n)]
    lastAnswer = 0
    res = []
    for q in queries:
        index = (q[1] ^ lastAnswer) % n

        if q[0] == 1:
            seqList[index].append(q[2])
        else:
            position = q[2] % len(seqList[index])
            lastAnswer = seqList[index][position]
            res.append(lastAnswer)
    for i in res:
        print(i)



if __name__ == '__main__':

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
