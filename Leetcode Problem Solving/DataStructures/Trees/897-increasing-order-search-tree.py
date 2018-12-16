# https://leetcode.com/problems/increasing-order-search-tree/description/
from BaseBST import genTree, TreeNode, printTree

# Store the inorder sequence in to a list
# Make the first element of the list as root
# For every remanining element in list, add them as right child to the root
def increasingBST(root):
    if not root: return None
    inorderList = []
    def inorder(root):
        if root:
            inorder(root.left)
            inorderList.append(root.val)
            inorder(root.right)
    inorder(root)
    root = TreeNode(inorderList[0])
    node = root
    for i in inorderList[1:]:
        node.right = TreeNode(i)
        node = node.right

    return root


root = genTree("[5,3,6,2,4,null,8,1,null,null,null,7,9]")
increasingBST(root)
