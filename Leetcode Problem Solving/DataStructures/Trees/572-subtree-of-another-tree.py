from BaseBST import genTree
# For each node in tree, check if that subtree is equal to the target subtree
# If not, then if its left node or right right node matches the target
# If there is no more nodes to check, means there hasn't been any matching subtree, then return false
# In the match method, if the tree and target nodes are equal and their left and right subtrees are also equal until there are no nodes
#  in both trees, return true
# If there are nodes left in one of the subtrees, then return False
def isSubtree(tree, subtree):

    def match(tree, subtree):
        if not tree and not subtree: return True
        if not tree or not subtree: return False
        # The above two lines can also also be combined written as -> if not (tree and subtree): return tree is subtree

        return tree.val == subtree.val and \
               match(tree.left, subtree.left) and \
               match(tree.right, subtree.right)

    def dfs(tree, subtree):
        if not tree: return False
        if match(tree, subtree): return True
        return dfs(tree.left, subtree) or dfs(tree.right, subtree)

    return dfs(tree, subtree)


treeNode = genTree('[1,null,1,null,1,null,1,null,1,null,1,2]')
subtreeNode = genTree('[1,null,1,null,1,null,1,2]')

print(isSubtree(treeNode, subtreeNode))
