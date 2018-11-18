class SinglyLinkedListNode:
    def __init__(self, node_data): # Method for creating a node
        self.data = node_data
        self.next = None

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


#  Function for deleting the node
def deleteNode(head, position):
    if position == 0
        return head.next
    head.next = deleteNode(head.next, position-1);
    return head


llist_count = int(input()) # Number of nodes

llist = SinglyLinkedList() # instance for the head

for i in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

data = int(input())

position = int(input())

llist_head = deleteNode(llist.head, data, position)

# Printing the elements of the linked list
while(llist_head != None):
    print(llist_head.data)
    llist_head = llist_head.next
