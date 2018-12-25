# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
from BaseBST import TreeNode, printTree

# 1.Since the given list is sorted, we can choose the middle element to be root node
# 2. Then the list elements to the left of the middle element will be lesser and can form the left subtree
# 3. All the list elements to the right of the middle element will be greater and can form the right subtree
# 4. Form the left subtree from leftList and right tree from rightList
# 5. Call the function recursively until there are no elements left
def SortedToBST(nums):
    if nums == []: return None

    middle = len(arr)//2
    root = TreeNode(nums[middle])

    leftList = nums[:middle]
    rightList = nums[middle+1 :]

    if leftList: root.left = SortedToBST(leftList)
    if rightList: root.right = SortedToBST(rightList)

    return root

printTree(SortedToBST([-10,-3,0,5,9]))
