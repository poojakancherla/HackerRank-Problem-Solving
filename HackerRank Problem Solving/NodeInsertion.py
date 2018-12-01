import LinkedListBase as l

#  Function for inserting nodes
def insertNodeAtTail(head, data):
    if head == None:
        head = l.SinglyLinkedListNode(data)
        return head
    else:
        curr = head
        while(curr.next != None):
            curr = curr.next
        curr.next = l.SinglyLinkedListNode(data)
        return head


llist_count = int(input()) # Number of nodes

llist = l.SinglyLinkedList() # instance for the head

for i in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtTail(llist.head, llist_item)
    llist.head = llist_head

l.printLinkedList(llist.head) # Printing the elements of the linked list
