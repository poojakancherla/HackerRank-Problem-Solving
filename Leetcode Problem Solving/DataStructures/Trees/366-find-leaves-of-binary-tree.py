# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
from BaseBST import genTree, printTree

def findLeaves(root):
    isLeaf = lambda root: not root.left and not root.right
    if not root: return [], None

    if isLeaf(root): return [root.val], None # Append the leaf to list and kill the leaf

    # It is a intermediate node(it might have left and right children)
    leftLeaves, root.left = findLeaves(root.left)
    rightLeaves, root.right = findLeaves(root.right)

    childLeaves = leftLeaves + rightLeaves # Accumulated your child leaves

    return childLeaves, root

root = genTree('[1,2,3,4,5]')
op = []
while(root):
    leaves, root = findLeaves(root)
    op.append(leaves)
print(op)
