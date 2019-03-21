class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


###### Iterative ########

def reverseList_iter(head):
    currNode = head
    prevNode, nextNode = None, None
    while currNode:
        nextNode = currNode.next
        currNode.next = prevNode

        prevNode = currNode
        currNode = nextNode
    return prevNode


#####################################################################################################################################################


###### Recursive ######

def reverseList_rec(head):
    if not head: return None
    if not head.next: return head
    
    nextNode = head.next
    head.next = None
    rest = reverseList_rec(nextNode)
    nextNode.next = head

    return rest


######################################################################################################################################################


# Creating the linked list
head = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)

head.next = a
a.next = b
b.next = c
c.next = d

# newHead = reverseList_iter(head)
newHead = reverseList_rec(head)

# Printing the new list
curr = newHead
while(curr):
    print(curr.val)
    curr = curr.next