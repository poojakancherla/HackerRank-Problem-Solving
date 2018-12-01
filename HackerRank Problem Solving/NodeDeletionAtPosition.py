import LinkedListBase as l

#  Function for deleting the node
def deleteNode(head, position):
    if position == 0:
        return head.next
    head.next = deleteNode(head.next, position-1);
    return head


llist_count = int(input()) # Number of nodes

llist = l.SinglyLinkedList() # instance for the head

for i in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

data = int(input())
position = int(input())

llist_head = deleteNode(llist.head, data, position)

# Printing the elements of the linked list
l.printLinkedList(llist_head)
