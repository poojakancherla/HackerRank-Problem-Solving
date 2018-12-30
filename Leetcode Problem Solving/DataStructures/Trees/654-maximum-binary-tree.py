# https://leetcode.com/problems/maximum-binary-tree/description/
from BaseBST import printTree, TreeNode
# The root is the maximum number in the array
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number

def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums: return None
    maxNum = max(nums) # Finding the max in list to construct root
    maxIndex = nums.index(maxNum) #Finding index in order to form left list for left subtree and right list for right subtree

    root = TreeNode(maxNum) # forming the root
    root.left = constructMaximumBinaryTree(nums[:maxIndex]) #left subtree constructed from left elements of root element
    root.right = constructMaximumBinaryTree(nums[maxIndex + 1:]) # right subtree from right elements of root element

    return root


nums = [3,2,1,6,0,5]
printTree(constructMaximumBinaryTree(nums))
