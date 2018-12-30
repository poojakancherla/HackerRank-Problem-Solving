from BaseBST import genTree
from collections import deque
# Same like level order but return the reversed output list
def levelOrderBottom(root):
    if not root: return []
    queue = deque([root])

    def levelNodes(root):
        if not root: return []
        output = []

        while queue:
            levelList = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                levelList.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            output.append(levelList)
        return output[::-1]
    return levelNodes(root)

root = genTree('[3,9,20,null,null,15,7]')

print(levelOrderBottom(root))
