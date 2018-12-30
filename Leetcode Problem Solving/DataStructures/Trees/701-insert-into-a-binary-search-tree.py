# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
from BaseBST import genTree, printTree, TreeNode

# if there is no root, then just return the node of the given value
# Using recursion, check if the val is less than or greater than each node and according add it as a left or right node

def insertIntoBST(root, val):

    if not root: return TreeNode(val)
    if val < root.val: root.left = insertIntoBST(root.left, val)
    if val > root.val: root.right = insertIntoBST(root.right, val)

    return root

root = genTree('[4,2,7,1,3]')
printTree(insertIntoBST(root, 5))
