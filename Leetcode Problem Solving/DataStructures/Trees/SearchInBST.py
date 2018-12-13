#700. https://leetcode.com/problems/search-in-a-binary-search-tree/description/

from BaseBST import genTree, printTree

def searchBST(root, target):
    if not root: return []
    if root.val == target: # if root equals the target, return the root
        return root
    if target < root.val: # if target < root, search in its left subtree
        return searchBST(root.left, target)
    else:
        return searchBST(root.right, target) # if target > root, search in its right subtree


root = genTree("[4, 2, 7, 1, 3, null, null]")
printTree(searchBST(root, 2))
