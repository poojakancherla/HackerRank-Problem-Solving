# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

# Apply BST and in every level, for each node add its val to a list
# This list should become an empty list for every level, so that it only has the node values of that particular level
# Append this list to the output list everytime, such that the output is a list of lists
# Return the output
def levelOrder(root):
    if not root: return []

        dq = deque([root])
        output = []

        while(dq):
            rowNodes = []
            for _ in range(len(dq)):
                node = dq.popleft()
                rowNodes.append(node.val)
                if node.children: dq.extend(node.children)
            output.append(rowNodes)

        return output
