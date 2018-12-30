# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
from BaseBST import genTree
from collections import deque
import sys
# Applied the concept of bread first search to traverse through all the nodes in the binary tree
# THe second min should be greater than the smallest element but smallest among the other nodes
# According to the question, this binary tree is special in a way that the root is always the smallest element
def secondMin(root):
    q = deque([root])
    mini = root.val
    secondMin = sys.maxsize

    while q:
        node = q.popleft()

        if node.val != mini: secondMin = min(node.val, secondMin)

        if node.left: q.append(node.left)
        if node.right: q.append(node.right)


    return secondMin if secondMin != sys.maxsize else -1







root = genTree('[1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]')

print(secondMin(root))
