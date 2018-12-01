import LinkedListBase as l

# Function to print the elements of a linked list
def printLinkedList(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

llist_count = int(input())

llist = l.SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

printLinkedList(llist.head)
