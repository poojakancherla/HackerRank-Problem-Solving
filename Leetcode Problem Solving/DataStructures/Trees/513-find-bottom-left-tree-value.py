# https://leetcode.com/problems/trim-a-binary-search-tree/
from BaseBST import genTree
from collections import deque

# if there is a root, we will use BFS and store each level in a queue
# For each list, we will go through all the nodes and store their left and right nodes into a list
# Update the queue with the list and repeat until the last level
# Keep track of the left most node which is the first element in the queue
#  Return the result

def findBottomLeftValue(root):
    if not root: return None

    def leftBottom(root):
        queue = [root]
        leftMost = queue[0]
        while queue:
            nextLevel = []
            for node in queue:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            queue = nextLevel
            if queue: leftMost = queue[0]
        return leftMost.val

    return leftBottom(root)

root = genTree('[1,2,3,4,null,5,6,null,null,7]')
print(findBottomLeftValue(root))
