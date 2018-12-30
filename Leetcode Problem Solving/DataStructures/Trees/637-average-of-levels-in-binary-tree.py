#  https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

from BaseBST import genTree

#  Perform BST on the genTree
#  For each level in tree, sum the node values and calculate the average
#  Append the result to list
#  For every level make the sum zero

def averageOfLevels(root):
    queue = [root]
    output = [root.val]
    while queue:
        nextLevel = []
        levelSum = 0.0
        for node in queue:
            if node.left: nextLevel.append(node.left); levelSum += node.left.val

            if node.right: nextLevel.append(node.right); levelSum += node.right.val

        queue = nextLevel
        if queue: output.append(levelSum/len(queue))

    return output

root = genTree('[3,9,20,null,null,15,7]')
print(averageOfLevels(root))
