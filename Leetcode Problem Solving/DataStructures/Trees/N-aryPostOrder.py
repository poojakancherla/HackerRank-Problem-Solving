# 590. https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

# To get the postorder sequence of N-ary tree:
# Push the root into a stack
# while the stack is not empty, pop the root, store it and push the children of the popped root into the stack
# repeat until the stack is empty

def postorder(root):
        if not root: return []

        stack = [root]
        l = []
        
        while stack:
            root = stack.pop()

            if root != None:
                l.append(root.val)

            if root.children:
                stack.extend(root.children)
        return l[::-1]
