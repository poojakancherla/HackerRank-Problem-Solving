# https://leetcode.com/problems/path-sum-iii/description/
from BaseBST import genTree

def pathSum(root, summ):
    count = [0]
    def checkSum(path, summ):
        tempSum = 0
        for i in range(len(path)-1, -1, -1):
            tempSum += path[i]
            if tempSum == summ: count[0] += 1

    def dfs(root, summ, path):
        if not root: return None
        path.append(root.val)
        checkSum(path, summ)
        dfs(root.left, summ, path)
        dfs(root.right, summ, path)
        path.pop()
    dfs(root, summ, [])
    return count[0]





root = genTree('[10,5,-3,3,2,null,11,3,-2,null,1]')

print(pathSum(root, 8))
