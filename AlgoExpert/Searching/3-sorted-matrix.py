def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row <= len(matrix) and col >= 0:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return [row, col]

print(searchInSortedMatrix([
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
], 44))