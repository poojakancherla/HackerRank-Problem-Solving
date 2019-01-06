from BaseBST import genTree
from collections import deque


########################################################################################################################

# Algorithm:
# Need to make a list of the nodes in a level and then compare if it is equal to its reversed list
# If there is a node in the queue, then check if it has left and right child. If no child, append None to the queue
# If thenode in the queue is None, then append None in the level list
def symmetricBFS(root):
    if not root: return True

    def bfs(root):
        q = deque([root])

        while q:
            levelNodes = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    levelNodes.append(node.val)
                    if node.left: q.append(node.left)
                    else: q.append(None)
                    if node.right: q.append(node.right)
                    else: q.append(None)
                else: levelNodes.append(None)
            if levelNodes != list(reversed(levelNodes)): return False
        return True

    return bfs(root)

##########################################################################################################################

def symmetricDFS(root):

    if not root: return True

    def mirror(left, right):
        if left and right: return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
        return left is right

    return mirror(root.left, root.right)

############################################################################################################################

root = genTree('[1,2,2,null,3,null,3]')

# print(symmetricBFS(root))
print(symmetricDFS(root))
