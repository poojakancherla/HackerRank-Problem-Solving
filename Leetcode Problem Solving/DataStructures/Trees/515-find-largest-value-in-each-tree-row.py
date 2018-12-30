# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
import sys
from BaseBST import genTree
from collections import deque

def largest(root):
    if not root: return []
    l = []
    queue = deque([root])
    while queue:
        maxi = -sys.maxsize
        elementsInTheLevel = len(queue)
        # the loop runs for nodes in that particular level
        # checks the maximum value only in those elements and not for all the elements in the queue
        # for example: the first level contains only root. So runs only once and the max value becomes 1
        # the next level contains its left and right and the max is found only in these elements
        # Even if the queue contains other elements, the max value is updated and then loop is re-initialized
        for i in range(elementsInTheLevel):
            curr = queue.popleft()
            maxi = max(curr.val, maxi)

            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)

        l.append(maxi)
    return l

root = genTree('[1, 3, 2, 5, 3, null, 9]')

print(largest(root))
