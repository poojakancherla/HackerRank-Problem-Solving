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

def length(head):
    counter = 0

    if head:
        curr = head

        while(curr):
            counter += 1
            curr = curr.next

    return counter


#  Function for comparing the two lists
def compare_lists(llist1, llist2):

    l1 = length(llist1)
    l2 = length(llist2)

    if l1 != l2:
        return 0

    while llist1:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    return 1



tests = int(input()) # No. of test cases

for tests_itr in range(tests):
    llist1_count = int(input())

    llist1 = SinglyLinkedList() # Defining the head of linked list 1

    for _ in range(llist1_count): # Inserting the nodes into linked list 1
        llist1_item = int(input())
        llist1.insert_node(llist1_item)

    llist2_count = int(input())

    llist2 = SinglyLinkedList() # Defining the head of linked list 2

    for _ in range(llist2_count): # Inserting the nodes into linked list 2
        llist2_item = int(input())
        llist2.insert_node(llist2_item)

    result = compare_lists(llist1.head, llist2.head) # Passing the heads of the linked lists

    print(result)
