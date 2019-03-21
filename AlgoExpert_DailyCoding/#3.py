# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
from BaseBST import printTree

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def helper(root):
        if not root: vals.append('#')
        else:
            vals.append(str(root.val))
            helper(root.left)
            helper(root.right)

    vals = []
    helper(root)
    return '[' + ','.join(vals) + ']'

def deserialize(data):
    def helper(root):
        val = next(vals)
        if val == '#': return None
        root = Node(int(val))
        root.left = helper(root)
        root.right = helper(root)
        return root
    vals = iter(data[1:-1].split(','))
    return helper(root)

    
root = Node("1")
root.left = Node("2")
root.left.left = Node('6')
root.right = Node("3")

data = serialize(root)
print(data)
deserialized_root = deserialize(data)
from BaseBST import printTree
printTree(deserialized_root)
