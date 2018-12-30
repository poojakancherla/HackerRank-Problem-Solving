# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

from BaseBST import genTree
from collections import deque

def common(root, p, q):
    def dfs(root, p, q):
        if not root: return None
        if p > root.val: return dfs(root.right, p, q)
        elif q < root.val:return dfs(root.left, p, q)
        else: return root

    return dfs(root, min(p, q), max(p, q)).val

root = genTree('[6,2,8,0,4,7,9,null,null,3,5]')

print(common(root, 8, 9))
