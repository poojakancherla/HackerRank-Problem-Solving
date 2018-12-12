from BaseBST import genTree, printTree


def mergeTrees(t1, t2):

    if not t1 and not t2: return None
    if not t2: return t1
    if not t1: return t2

    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)

    return t1

t1 = genTree("[1,3,2,5]")
t2 = genTree("[2,1,3,null,4,null,7]")

printTree(mergeTrees(t1, t2))
