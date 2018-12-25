from BaseBST import genTree, printTree
from collections import deque

def invertTreeRecursive(root):
    if not root: return None

    root.right, root.left = invertTreeRecursive(root.left), invertTreeRecursive(root.right)

    return root

def invertTreeBFS(root):
    if not root: return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return root

root = genTree('[4,2,7,1,3,6,9]')

# printTree(invertTreeRecursive(root))

printTree(invertTreeBFS(root))
