# https://leetcode.com/problems/trim-a-binary-search-tree/

from BaseBST import genTree, printTree

#  if root is less than the left range value, then we pass the root and its left subtree and trim from the right node onwards
#  if root is greater than the right range value, then we pass the root and its right subtree and trim from the left node onwards
#  repeat this until there is no node and then return the root
def trimBST(root, L, R):
    def trim(root):
        if not root: return None
        if root.val < L: return trim(root.right)
        elif root.val > R: return trim(root.left)
        else: root.left = trim(root.left); root.right = trim(root.right)
        return root
    return trim(root)


root = genTree('[3,0,4,null,2,null,null,1]')
printTree(trimBST(root, 1, 3))
