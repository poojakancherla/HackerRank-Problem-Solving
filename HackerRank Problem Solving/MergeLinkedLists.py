import LinkedListBase as l

def mergeLists(head1, head2):
    a = head1
    b = head2
    start_node = l.SinglyLinkedListNode("x")
    curr = start_node

    while a and b:
        if a.data < b.data:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next

    curr.next = a or b
    
    return start_node.next


t = int(input()) # test cases

for i in range(t):
    n = int(input()) # length of first linked list
    llist1 = l.SinglyLinkedList()
    for _ in range(n):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)

    m = int(input()) # length of second linked list
    llist2 = l.SinglyLinkedList()
    for _ in range(m):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)

    llist3 = mergeLists(llist1.head, llist2.head)

l.printLinkedList(llist3)
