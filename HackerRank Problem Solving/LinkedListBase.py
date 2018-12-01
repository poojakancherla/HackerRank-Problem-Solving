class SinglyLinkedListNode:
    def __init__(self, node_data): # Method for creating a node
        self.data = node_data
        self.next = None

class DoublyLinkedListNode:
    def __init__(self, node_data): # Method for creating a node
        self.data = node_data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def length(head):
    counter = 0

    if head:
        curr = head

        while(curr):
            counter += 1
            curr = curr.next

    return counter

def genList():
    data = list(map(int, input().split()))

    head = LinkedList(data[0])
    linkedlist = head

    for i in data[1:]:
        linkedlist.next = LinkedList(i)
        linkedlist = linkedlist.next
    return head

# Function to print the elements of a linked list
def printLinkedList(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next
