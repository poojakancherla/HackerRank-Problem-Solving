# https://leetcode.com/problems/diameter-of-binary-tree/description/
from BaseBST import genTree
from collections import deque

def diameter(root):
    result = [0]
    def depth(root):
        if not root: return 0

        left = depth(root.left)
        right = depth(root.right)

        result[0] = max(result[0], left + right)
        return 1 + max(left, right)
    depth(root)
    return result[0]

root = genTree('[1,2,3,4,5,4,5,5,null,null,2,2,2,2,2,2,null,null,null,null,2,2,2,2,2,2,2,2]')

print(diameter(root))
