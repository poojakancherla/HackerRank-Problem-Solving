# 559.https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

### Algorithm using Recursion and DFS ###
# If there is no root, the height is zero
# If there is a root, then apply dfs to traverse to each of the leaf nodes
# Store all these heights in a list
#  If there is no further children for a node, return 1 for that node
#  Find the max of the list and add 1 for the root node

def maxDepth(root):
        if not root: return 0

        def findDepth(root):
            if not root.children: return 1
            maxChildDepth = max([findDepth(child) for child in root.children])
            return maxChildDepth + 1

        return findDepth(root)


###  Iterative Algorithm using BFS ###
# If there is no root, return 0
# Else, add the root to the queue
# While the queue is not empty, increment max_depth and then pop a node from left
# If the popped node has children, add them to the queue
# Finally return max_depth

def maxDepth(root):
        if not root: return 0

        max_depth = 0
        dq = deque([root])

        while dq:
            max_depth += 1

            for _ in range(len(dq)):
                node = dq.popleft()
                if node.children: dq.extend([child for child in node.children])

        return max_depth
