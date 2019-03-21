class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        printTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        printTree(node.left, prefix + ("    " if isLeft else "│   "), True)

def genTree(dataList = [], customInput = False):
    if customInput:
        dataList = input().strip()
    else:
        dataList = dataList[1:-1].replace(",", " ")

    if not dataList:
        return None

    dataListValues = [s.strip() for s in dataList.split()]
    root = TreeNode(int(dataListValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(dataListValues):
        node = nodeQueue[front]
        front = front + 1

        item = dataListValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(dataListValues):
            break

        item = dataListValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    printTree(root)
    return root


def genListOfTree(root, addChildNulls = True):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            if addChildNulls: output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.val)
        inorder(root.right)
        
def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = genTree(line)
            printTree(node)
        except StopIteration:
            break
