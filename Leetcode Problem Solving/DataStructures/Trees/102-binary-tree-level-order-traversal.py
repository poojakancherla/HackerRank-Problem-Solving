# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from BaseBST import genTree
from collections import deque
def levelOrder(root):
    if not root: return []
    queue = deque([root])
    # Do a BFS traversal
    def levelNodes(root):
        output = [] # List to store the final result
        if not root: return []
        while queue:
            nodes = [] # List to store the nodes for the particular level and will be renewed every time the loop ends for a level
            for _ in range(len(queue)): # Each time the loop runs only for the number of nodes in a level
                node = queue.popleft() # Pop the value and store it in a list
                nodes.append(node.val) # Since the loop limits to only the level nodes, the list contains the same
                if node.left: queue.append(node.left) # if the node has any left child add it to the queue
                if node.right: queue.append(node.right) # if the node has any right child add it to the queue

            output.append(nodes) # Keep appending the lists for each level
        return output # return the output
    return levelNodes(root) # call the BFS function



root = genTree('[3,9,20,null,null,15,7]')

print(levelOrder(root))
