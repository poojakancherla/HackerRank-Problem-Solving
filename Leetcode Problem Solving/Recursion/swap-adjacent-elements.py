class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def swap(head):
    dummy = Node('x')
    dummy.next = head

    prev, t1, t2, next = dummy, None, None, None

    while(head and head.next):
        t1 = head
        t2 = head.next

        nextList = t2.next
        t1.next = nextList
        t2.next = t1
        prev.next = t2
        prev = t1
        head = nextList

    return dummy.next


head = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)

head.next = a
a.next = b
b.next = c
c.next = d

newHead = swap(head)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next.val)
print(newHead.next.next.next.val)
print(newHead.next.next.next.next.val)
