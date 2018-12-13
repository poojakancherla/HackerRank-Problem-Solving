# 589. https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/187092/Python-Iterative-and-Recursive-solutions

# To get the preorser sequence of N-ary tree:
# Push the root into a stack
# while the stack is not empty, pop the root and push the children from right to left of the popped root into the stack
# repeat until the stack is empty

def preorder(root):
    if not root: return []

    stack = [root]
    l = [] # Storing the sequence into a list
    while stack:
        curr = stack.pop() # pop the root
        l.append(curr.val) # add the value to list
        stack.extend(reversed(curr.children)) # add the children of the popped root from right to left
    return l
