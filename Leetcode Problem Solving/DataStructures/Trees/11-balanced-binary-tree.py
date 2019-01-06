from BaseBST import genTree
def balancedBinaryTree(root):
    def dfsDepth(root):
        if not root: return 0

        leftDepth = dfsDepth(root.left)
        if leftDepth == -1: return -1

        rightDepth = dfsDepth(root.right)
        if rightDepth == -1: return -1
        
        if abs(leftDepth - rightDepth) > 1: return -1
        return max(leftDepth, rightDepth) + 1
    return dfsDepth(root) > -1

    # return dfsDepth(root) > -1
    def height(root):
        if not root: return 0
        return 1 + max(height(root.right), height(root.left))

    def dfs(root):
        if not root: return True
        left = height(root.left)
        right = height(root.right)
        return abs(left - right) <= 1 and dfs(root.left) and dfs(root.right)

    return dfs(root)

root = genTree('[3,9,20,null,null,15,7]')
print(balancedBinaryTree(root))
