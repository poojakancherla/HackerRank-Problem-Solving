# https://leetcode.com/problems/path-sum/description/
from BaseBST import genTree
def hasPathSum(root, summ):
    # if not root: return False
    # sum -= root.val
    # if not root.left and not root.right: return sum == 0
    # return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

    count = [0]
    # result = []
    def dfs(root, summ, path):
        if not root: return None
        path.append(root.val)
        if not root.left and not root.right:
            if sum(path) == summ:
                # result.append(path[:])
                count[0] += 1
        dfs(root.left, summ, path)
        dfs(root.right, summ, path)
        path.pop()

    dfs(root, summ, [])
    # print(result)
    return True if count[0] else False

root = genTree('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
print(hasPathSum(root, 22))
