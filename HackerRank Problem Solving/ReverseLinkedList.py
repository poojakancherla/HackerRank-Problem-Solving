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

#  Function to reverse the linked list
def reverse(head):
    if head == None:
        return head
    else:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        return prev


tests = int(input())

for tests_itr in range(tests):
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)

# Printing the elements of the linked list
while llist1:
    print(llist1.data)
    llist1 = llist1.next
