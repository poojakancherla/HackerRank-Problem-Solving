from TreeBase import genTree
import sys

def minDiffInBST(root): 
    pre = [-sys.maxsize]
    minDiff = [sys.maxsize]
    def dfs(root):        
        if not root: return
        dfs(root.left)
        minDiff[0] = min(minDiff[0], root.val - pre[0])
        pre[0] = root.val
        dfs(root.right)
    dfs(root)
    return minDiff[0]


# class Solution:
#     def __init__(self):
#         self.pre = -sys.maxsize
#         self.minDiff = sys.maxsize

#     def minDiffInBST(self, root):          
#         def dfs(root):
#             if not root: return
#             dfs(root.left)
#             self.minDiff = min(self.minDiff, root.val - self.pre)
#             self.pre = root.val
#             dfs(root.right)
#         dfs(root)
#         return self.minDiff

root = genTree('[4,2,6,1,3,null,null]')
print(minDiffInBST(root))