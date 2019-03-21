###### Iterative solution #######
def generate(numRows):
    if not numRows: return []
    output = [[1]]
    for _ in range(1, numRows):
        lastRow = output[-1]
        nextRow = []
        for i in range(len(lastRow)-1):
            nextRow.append(lastRow[i] + lastRow[i+1])
        output.append([1] + nextRow + [1])

    return output
# print(generate(5))




##### Recursive solution ######
def generate_rec(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]    
    
    output = generate_rec(numRows - 1)
    lastRow = output[-1]
    nextRow = [1]
    for i in range(len(lastRow) - 1):
        nextRow.append(lastRow[i] +  lastRow[i+1])
    nextRow += [1]
    output.append(nextRow)

    return output

print(generate_rec(5))

