# https://leetcode.com/problems/closest-binary-search-tree-value/description/

from BaseBST import genTree
import sys
def closestValue(root, target):

    def run(root, target):

        closest = [sys.maxsize, None] # This array is used to store the current node value and its diff with the target

        if abs(root.val - target) < closest[0]: # If the curr node's diff is less than that of the previous node
            closest[0] = abs(root.val - target) # update the new difference
            closest[1] = root.val # update the new node value

        if root.left: # traversing through the left nodes
            closest = min(closest, run(root.left, target))
        if root.right: # traversing through the right nodes
            closest = min(closest, run(root.right, target))
        return closest

    return run(root, target)[1]

root = genTree('[1, null, 2]')
print(closestValue(root, 3.714286))
