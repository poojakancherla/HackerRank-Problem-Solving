from BaseBST import genTree

def leafSimilar(root1, root2):
    def getLeaf(root):
        if not root: return None

        leaves = []
        if not root.left and not root.right: leaves.append(root.val)

        if root.left: leaves += getLeaf(root.left)
        if root.right: leaves += getLeaf(root.right)

        return leaves




    # leaves = []
    # getLeaf(root1)
    # treeLeaves1 = leaves
    # leaves = []
    # getLeaf(root2)
    # treeLeaves2 = leaves

    # print(treeLeaves1, treeLeaves2)
    return(getLeaf(root1) == getLeaf(root2))


t1 = "[3,5,1,6,2,9,8,null,null,7,4]"
t2 = "[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]"
root1 = genTree(t1)
root2 = genTree(t2)

print(leafSimilar(root1, root2))
