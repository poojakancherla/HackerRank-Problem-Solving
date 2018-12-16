from BaseBST import genTree

# getLeaf method checks if there is a root. If there is a root and if doesn't have have any children, then it is the leaf node
# This leaf as added to the leaves array
# If the root node has a left child, then we iteraitively check if it is the leaf nodeand then append it to the list
# Same process if the root has a right child
# Return the leaves array
# Now compare the getLeaves method for both the trees and return true or false 

def leafSimilar(root1, root2):
    def getLeaf(root):
        if not root: return None

        leaves = []
        if not root.left and not root.right: leaves.append(root.val)

        if root.left: leaves += getLeaf(root.left)
        if root.right: leaves += getLeaf(root.right)

        return leaves

    return(getLeaf(root1) == getLeaf(root2))


t1 = "[3,5,1,6,2,9,8,null,null,7,4]"
t2 = "[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]"
root1 = genTree(t1)
root2 = genTree(t2)

print(leafSimilar(root1, root2))
