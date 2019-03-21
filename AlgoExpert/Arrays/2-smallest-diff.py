def smallestDifference(arrayOne, arrayTwo):

    i = j = 0
    minDiff = float("inf")
    currDiff = float("inf")
    smallestPair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        firstNum = arrayOne[i]
        secondNum = arrayTwo[j]

        if firstNum == secondNum: return [firstNum, secondNum]

        if firstNum < secondNum:
            currDiff = secondNum - firstNum
            i += 1
        else:
            currDiff = firstNum - secondNum
            j += 1

        if currDiff < minDiff:
            minDiff = currDiff
            smallestPair = [firstNum, secondNum]


    return smallestPair

print(smallestDifference([240,124,86,111,2,84,954,27,89], [1,3,954,19,8]))
