class SinglyLinkedListNode:
    def __init__(self, node_data): # Method for creating a node
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

#  Function for inserting nodes
def insertNodeAtHead(llist, data):
    head = llist
    if head == None:
        head = SinglyLinkedListNode(data)
        return head
    else:
        next_node = head
        head = SinglyLinkedListNode(data)
        head.next = next_node
        return head

llist_count = int(input()) # Number of nodes

llist = SinglyLinkedList() # instance for the head

for i in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtHead(llist.head, llist_item)
    llist.head = llist_head

# Printing the elements of the linked list
while(llist_head != None):
    print(llist_head.data)
    llist_head = llist_head.next
