import LinkedListBase as l

#  Function for inserting nodes
def insertNodeAtHead(llist, data):
    head = llist
    if head == None:
        head = l.SinglyLinkedListNode(data)
        return head
    else:
        next_node = head
        head = l.SinglyLinkedListNode(data)
        head.next = next_node
        return head

llist_count = int(input()) # Number of nodes

llist = l.SinglyLinkedList() # instance for the head

for i in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtHead(llist.head, llist_item)
    llist.head = llist_head

# Printing the elements of the linked list
l.printLinkedList(llist_head)
