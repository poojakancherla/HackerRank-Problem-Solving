# https://leetcode.com/problems/binary-tree-pruning/description/

from BaseBST import genTree, TreeNode, printTree

# 1. First, we need to check if the left and right subtrees of a node contain a one
# 2. If there is no one, return None for the subtree(means prune it)
# 3. If there is one, return the root for the subtree
# 4. This will recursively happen in postOrder traversal
# 5. If the root is 1, return root
# 6. If root is 0, and if both left tree and right tree of the root return None, then return None for that root

# The process starts from the left most node which is a leaf node which is sent as root to pruneTree
# If the root is 1, return root
# If root is 0, and since it does not have left or right nodes, it will return None(since no 1)
# Then the function checks next leaf node, and returns root or none
# If both these leaf nodes returned None, and if the root is 0, then return None
# But if the root is 1, then return root
# The function keeps returning root or None for all the nodes of the Binary Tree



def pruneTree(root):
    if not root: return None

    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)

    if root.val == 1: return root

    if root.val == 0:
        if not root.left and not root.right: return None

    return root




root = genTree('[1,0,1,0,0,0,1]')
printTree(pruneTree(root))

    #
    #
    #
    # if not root: return None
    # node = root
    # def containsOne(node):
    #     if node.val == 0 and (pruneTree(node.left) != 1 or pruneTree(node.right) != 1):
    #         return False
    #     return True
    #
    # if not containsOne(node.left) and not containsOne(node.right):
    #     return None
