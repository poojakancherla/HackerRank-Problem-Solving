# 104. https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from BaseBST import genTree
from collections import deque

def maxDepthBFS(root):
    if not root: return 0
    dq = deque([root])
    maxDepth = 0

    while dq:
        maxDepth += 1

        for i in range(len(dq)):
            curr = dq.popleft()

            if curr.left: dq.append(curr.left)
            if curr.right: dq.append(curr.right)
    return maxDepth






root = genTree("[3, 9, 20, null, null, 15, 7]")
print(maxDepthBFS(root))





def maxDepthDFS(root):
    if not root: return 0

    def findDepth(root):
        leftDepth = rightDepth = 0

        if root.left: leftDepth = findDepth(root.left)
        if root.right: rightDepth = findDepth(root.right)

        return max(leftDepth, rightDepth) + 1
    return findDepth(root)

root = genTree("[3, 9, 20, null, null, 15, 7]")
print(maxDepthDFS(root))
