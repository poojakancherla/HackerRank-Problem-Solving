# Given the root to a binary tree, count the number of unival subtrees.
from BaseBST import genTree


def unival1(root):
    def isUnival(root):
        if not root: return True
        if root.left and root.left.val != root.val: return False
        if root.right and root.right.val != root.val: return False
        if isUnival(root.left) and isUnival(root.right): return True
        return False

    def countUnivals(root):
        if not root: return 0
        total = countUnivals(root.left) + countUnivals(root.right)
        if isUnival(root): total += 1
        return total

    return countUnivals(root)

def unival2(root):
    def countUnivals(root):
        total, isUnival = helper(root)
        return total
    def helper(root):
        if not root: return (0, True)
        leftCount, isLeftUnival = helper(root.left)
        rightCount, isRightUnival = helper(root.right)
        isUnival = True
        if not isLeftUnival or not isRightUnival: isUnival = False
        if root.left and root.left.val != root.val: isUnival = False
        if root.right and root.right.val != root.val: isUnival = False
        if isUnival: return (leftCount + rightCount + 1, True)
        else: return (leftCount + rightCount, False)

    return countUnivals(root)

root = genTree('[0,1,0,null,null,1,0,1,1,null,null]')
# root = genTree('[1,1,1]')
print(unival2(root))
